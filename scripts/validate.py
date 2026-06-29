#!/usr/bin/env python3
"""Validate the qhse skill before packaging.

Checks (errors fail the build):
  1. Frontmatter — required fields, name format, name == folder, frontmatter <= 1024 chars
  2. Reference files — every `references/X.md` mentioned actually exists
  3. Section refs — every `file.md §N` cross-reference resolves to a real heading
  4. Regressions — MUST-NOT strings never reappear
  5. Hygiene — no TODO/FIXME/XXX markers or merge-conflict markers

Usage: python3 scripts/validate.py
Exit code 0 = pass, 1 = one or more errors.
"""
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_DIR = os.path.join(ROOT, "qhse")
REF_DIR = os.path.join(SKILL_DIR, "references")
SKILL_MD = os.path.join(SKILL_DIR, "SKILL.md")

errors = []
warnings = []

def rel(p):
    return os.path.relpath(p, ROOT)

def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()

skill_md_files = (
    [SKILL_MD]
    + sorted(glob.glob(os.path.join(REF_DIR, "*.md")))
)
ref_files = {os.path.basename(p) for p in glob.glob(os.path.join(REF_DIR, "*.md"))}

# --- 1. Frontmatter -------------------------------------------------------
text = read(SKILL_MD)
m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
if not m:
    errors.append("SKILL.md: missing YAML frontmatter")
else:
    fm = m.group(1)
    if len(fm) > 1024:
        errors.append(f"SKILL.md frontmatter exceeds 1024 chars ({len(fm)})")
    name_m = re.search(r"^name:\s*(.+)$", fm, re.M)
    if not name_m:
        errors.append("SKILL.md frontmatter: missing 'name'")
    else:
        nm = name_m.group(1).strip()
        if not re.fullmatch(r"[a-z0-9-]+", nm):
            errors.append(f"SKILL.md name '{nm}' must be lowercase letters/numbers/hyphens only")
        if nm != "qhse":
            errors.append(f"SKILL.md name '{nm}' must equal folder name 'qhse'")
    if not re.search(r"^version:\s*\d+\.\d+\.\d+\s*$", fm, re.M):
        errors.append("SKILL.md frontmatter: missing or non-semver 'version'")
    if not re.search(r"^description:\s*", fm, re.M):
        errors.append("SKILL.md frontmatter: missing 'description'")

# --- 2. Reference-file resolution ----------------------------------------
for p in skill_md_files:
    t = read(p)
    for mm in re.finditer(r"references/([a-z0-9-]+\.md)", t):
        fn = mm.group(1)
        if fn not in ref_files:
            errors.append(f"{rel(p)}: links to references/{fn} which does not exist")

# --- 3. Section-reference resolution --------------------------------------
sec_index = {}
for fn in ref_files:
    t = read(os.path.join(REF_DIR, fn))
    sec_index[fn] = set(re.findall(r"^#{2,3}\s+(\d+)\.", t, re.M))

xref_re = re.compile(r"`?([a-z0-9-]+\.md)`?\s*§\s*(\d+)")
for p in skill_md_files:
    t = read(p)
    for mm in xref_re.finditer(t):
        fn, sec = mm.group(1), mm.group(2)
        if fn in sec_index and sec not in sec_index[fn]:
            errors.append(f"{rel(p)}: cross-ref {fn} §{sec} -> no heading in {fn}")

# --- 4. Regression guard --------------------------------------------------
must_not = [
    (r"Code de l'Environnement 2023-15", "use correct form 'Loi n° 2023-15'"),
]
for p in skill_md_files:
    t = read(p)
    for pat, why in must_not:
        for mm in re.finditer(pat, t):
            ln = t[: mm.start()].count("\n") + 1
            errors.append(f"{rel(p)}:{ln}: regression — {why} [matched: {mm.group(0)!r}]")

# --- 5. Hygiene -----------------------------------------------------------
for p in skill_md_files:
    t = read(p)
    for pat in (r"\[verify", r"\bTODO\b", r"\bFIXME\b", r"\bXXX\b", r"^(<<<<<<<|=======|>>>>>>>)"):
        for mm in re.finditer(pat, t, re.M):
            ln = t[: mm.start()].count("\n") + 1
            errors.append(f"{rel(p)}:{ln}: leftover marker {mm.group(0)!r}")

# --- report ---------------------------------------------------------------
for w in warnings:
    print(f"WARN  {w}")
for e in errors:
    print(f"ERROR {e}")

print()
print(f"{len(ref_files)} reference files | {len(warnings)} warnings | {len(errors)} errors")
sys.exit(1 if errors else 0)
