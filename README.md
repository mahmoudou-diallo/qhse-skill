[![skills.sh](https://skills.sh/b/mahmoudou-diallo/qhse-skill)](https://skills.sh/mahmoudou-diallo/qhse-skill)

# QHSE Skill — Quality, Health, Safety, Environment

Skill QHSE compatible avec **tous les agents LLM** : Claude Code, OpenCode, Cursor, Windsurf, Cline, Roo Code, Gooses, Antigravity, Gemini, GitHub Copilot, Codex, et tout agent supportant les skills au format standard.

Professionnels QHSE en Afrique de l'Ouest.

Couvre ISO 9001 (Qualité), ISO 14001:2026 (Environnement), ISO 45001 (SST),
le Code du Travail sénégalais, le Code de l'Environnement 2023-15,
le Décret 2025-227, et les cadres UEMOA/CEDEAO.

## Structure

```
qhse-skill/
├── qhse/                     # 📦 Skill folder (ce dossier est le skill)
│   ├── SKILL.md              # Point d'entrée + routage
│   └── references/
│       ├── company.md        # Contexte organisationnel (à remplir)
│       ├── standards.md      # ISO 9001, 14001:2026, 45001
│       ├── senegal.md        # Réglementation Sénégal/Afrique Ouest
│       ├── tools.md          # Outils QHSE open-source
│       └── templates.md      # Templates inspection, incident, CAPA, JSA
├── scripts/
│   └── validate.py           # Validation CI (frontmatter, refs, hygiene)
├── .github/workflows/
│   └── package.yml           # CI: validation + packaging .zip / .skill
├── README.md
└── LICENSE
```

## Installation

### OpenCode (local)

```bash
cp -r qhse/ ~/.config/opencode/skills/qhse/
```

### Claude.ai / Claude Code / Antigravity / Hermes

1. Télécharger `qhse-skill.zip` depuis la dernière [Release](https://github.com/mahmoudou-diallo/qhse-skill/releases)
2. Settings → Skills → Upload skill

### Cursor / Windsurf / Cline / Roo Code / Gooses

```bash
# Glisser-déposer le dossier qhse/ dans l'interface du skill
# Ou pointer le chemin local vers le dossier
```

### skills.sh (bientôt)

```bash
npx skills install mahmoudou-diallo/qhse-skill
```

## Utilisation

Charger le skill avant une tâche QHSE :

- Inspection sécurité → `references/templates.md`
- Audit ISO 14001:2026 → `references/standards.md`
- Conformité Code du Travail → `references/senegal.md`
- Analyse de risques HIRA → `references/standards.md` §4

## Personnalisation

1. Copier le dossier
2. Remplir `references/company.md` avec vos données
3. Ajuster les templates si nécessaire

## License

CC BY-SA 4.0
