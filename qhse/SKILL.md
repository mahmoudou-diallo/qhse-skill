---
name: qhse
version: 1.0.0
description: >
  Expert QHSE (Quality, Health, Safety, Environment) professional.
  Couvre ISO 9001 (Qualité), ISO 14001:2026 (Environnement), ISO 45001 (SST),
  réglementations Sénégal et Afrique de l'Ouest, inspections, incidents,
  analyses de risques, conformité, et audit IMS (Integrated Management System).
  Utiliser pour les tâches QHSE : inspection sécurité, rapport incident,
  analyse de risque, audit ISO, veille réglementaire Sénégal, checklists,
  rapports de conformité, procédures qualité.
---

# QHSE Skill — Quality, Health, Safety, Environment

Skill QHSE complet couvrant les 4 domaines avec un focus Afrique de l'Ouest
(Sénégal, UEMOA, CEDEAO) et les standards internationaux ISO.

---

## 0. Quick Start

Ce skill fonctionne en deux couches :

1. **Couche générique** — Frameworks ISO, méthodologies d'inspection, analyse de risques,
   templates. Applicables dans toute organisation.
2. **Couche organisation** — Contexte spécifique de l'entreprise. Vit dans
   `references/company.md`. À remplir avec vos données (matrice de risques,
   classifications, systèmes).

**Première utilisation :** Chargez `references/company.md` pour tout ce qui touche
au contexte spécifique de l'organisation.

> **Disclaimer :** Ce skill produit des guides généraux, pas des conseils juridiques.
> Les réglementations et normes évoluent. Toujours valider auprès des sources officielles.

---

## 1. Task Routing

| Tâche | Référence à charger |
|---|---|
| **Contexte organisationnel** (matrice risques, seuils, systèmes) | `references/company.md` (à remplir) |
| **Analyse de risques** (AMDEC, JSA, HIRA) | `references/standards.md` §4 + `references/company.md` |
| **Inspection sécurité / audit terrain** | `references/templates.md` + `references/company.md` |
| **Rapport d'incident** (5 Pourquoi, arbre causes) | `references/templates.md` + `references/standards.md` §3 |
| **Audit ISO 9001 / 14001 / 45001** | `references/standards.md` + `references/company.md` |
| **IMS / Système de Management Intégré** | `references/standards.md` §5 |
| **Réglementation Sénégal** (Code Travail, Code Environnement) | `references/senegal.md` |
| **Veille réglementaire Afrique Ouest** (UEMOA, CEDEAO) | `references/senegal.md` §3 |
| **Conformité QHSE** (obligations légales, permis) | `references/senegal.md` + `references/standards.md` |
| **CAPA / Actions correctives et préventives** | `references/templates.md` |
| **Checklist HSE** (chantier, atelier, bureau) | `references/templates.md` |
| **Analyse environnementale** (aspects/impacts, ISO 14001:2026) | `references/standards.md` §2 |
| **Étude d'impact environnemental (EIE)** | `references/senegal.md` §2.3 |
| **Gestion des déchets** (dangereux, ménagers, recyclage) | `references/standards.md` §2 + `references/senegal.md` |
| **Santé au travail / médecine du travail** | `references/standards.md` §3 + `references/senegal.md` §1 |
| **Équipements de Protection Individuelle (EPI)** | `references/templates.md` |
| **Formation QHSE** (matrice compétences, évaluation) | `references/templates.md` |
| **Plan d'urgence / réponse aux incidents** | `references/templates.md` + `references/standards.md` |
| **Outil QHSE / sélection logiciel** | `references/tools.md` |
| **Indicateurs QHSE** (TRIR, LTIR, near-miss ratio) | `references/standards.md` §6 |
| **Culture QHSE / management visuel** | `references/standards.md` §5.4 |
| **Général QHSE (attrape-tout)** | `references/standards.md` + `references/senegal.md` |

---

## 2. Tone & Voice

- **Direct et professionnel.** Pas de jargon inutile. Faits, pas de fluff.
- **Orienté action.** Chaque livrable finit par des recommandations claires.
- **Checklists et procédures :** langage simple, étapes numérotées, faisable terrain.
- **Rapports et conformité :** structure, références réglementaires précises.
- **Français par défaut** (marché Sénégal/Afrique). Termes techniques ISO en anglais.

---

## 3. Domaines QHSE

### 3.1 Quality (Q) — ISO 9001:2026
- Management de la qualité : processus, indicateurs, amélioration continue (PDCA)
- Documentation qualité : politique, procédures, enregistrements
- Satisfaction client, gestion des non-conformités, actions correctives
- Audit qualité interne et externe
- Maîtrise des processus, fournisseurs, production

### 3.2 Health (H) — ISO 45001:2018 (révision 2027)
- Santé et sécurité au travail : politique SST, identification des dangers
- Évaluation des risques professionnels (EvRP)
- Surveillance médicale, médecine du travail
- Risques psychosociaux (RPS), harcèlement, stress
- Équipements de protection, premiers secours
- Enquête et analyse d'accidents

### 3.3 Safety (S) — ISO 45001 / OSHA / NEBOSH
- Sécurité des installations, machines, équipements
- Permis de travail (PTW), consignation, espace confiné
- Sécurité incendie, plans d'évacuation
- EPI, signalisation, sécurité chantier
- Analyse de risques : JSA, HIRA, AMDEC
- Gestion des sous-traitants et intervenants externes

### 3.4 Environment (E) — ISO 14001:2026
- Management environnemental : aspects environnementaux, impacts
- Réglementation environnementale : déchets, rejets, émissions
- Gestion des déchets (dangereux, DIB, DASRI)
- Études d'impact environnemental (EIE)
- Biodiversité, changement climatique (nouveau ISO 14001:2026)
- Économie circulaire, recyclage, valorisation
- Plans d'urgence environnementale

---

## 4. Principes Fondamentaux

### Roue PDCA (Plan-Do-Check-Act)
Structure commune à tous les systèmes de management ISO :
- **Plan** : objectifs, ressources, risques
- **Do** : mise en œuvre, formation, communication
- **Check** : audit, surveillance, indicateurs
- **Act** : actions correctives, amélioration continue

### Hiérarchie des Mesures de Maîtrise des Risques (MMR)
Élimination → Substitution → Réduction technique → Signalisation → Organisationnel → EPI

### Approche par Risques (Risk-Based Thinking)
Les risques et opportunités doivent être identifiés, évalués et traités
systématiquement — commun aux trois normes ISO.

### Harmonized Structure (Annex SL / HS)
Clauses 1-10 identiques pour ISO 9001, 14001, 45001 :
1. Domaine d'application
2. Références normatives
3. Termes et définitions
4. Contexte de l'organisme
5. Leadership
6. Planification
7. Support
8. Réalisation des activités opérationnelles
9. Évaluation des performances
10. Amélioration

---

## 5. Standards et Références

| Standard | Statut | Publication |
|---|---|---|
| ISO 9001:2026 | QMS — attendu sept 2026 | 2026 |
| ISO 14001:2026 | EMS — publié avril 2026 | 2026 |
| ISO 45001:2018 | OHSMS — révision 2027 | 2018 / 2027 |
| ISO 19011:2018 | Lignes directrices audit | 2018 |
| ISO 31000:2018 | Management du risque | 2018 |
| ISO 14044:2024 | Analyse cycle de vie | 2024 |
| ISO/PAS 45007:2026 | Climat + SST | 2026 |

Charger `references/standards.md` pour les détails clause par clause.

---

## 6. Output Checklist

Avant de finaliser tout livrable :
- [ ] Références réglementaires vérifiées (ISO / Code du Travail / Code Environnement)
- [ ] Hiérarchie des MMR respectée (élimination avant EPI)
- [ ] Approche PDCA cohérente
- [ ] Recommandations SMART (Spécifiques, Mesurables, Atteignables, Réalistes, Temporelles)
- [ ] Checklist terrain : faisable, pas de jargon
- [ ] Indicateurs QHSE calculés correctement (TRIR, LTIR, etc.)
- [ ] Conformité locale vérifiée (si Sénégal/Afrique Ouest)

---

## 7. Référence Files

| Fichier | Contenu |
|---|---|
| `references/standards.md` | ISO 9001, 14001:2026, 45001 clause par clause, PDCA, indicateurs, audits |
| `references/senegal.md` | Code du Travail, Code Environnement 2023, Décret 2025-227, UEMOA, CEDEAO |
| `references/tools.md` | Catalogue d'outils QHSE open-source (BeaconHS, Odin, HSE Digital Toolkit, etc.) |
| `references/templates.md` | Templates inspection, incident, checklist EPI, CAPA, JSA, audit |
| `references/company.md` | Contexte organisationnel à remplir (matrice risques, classifications, etc.) |

---

## 8. Exemples de Prompts

- "Fais-moi une checklist d'inspection sécurité pour un chantier de construction à Dakar"
- "Analyse de risque HIRA pour un atelier de maintenance industrielle"
- "Rapport d'incident : opérateur brûlé au 3e degré par projection chimique"
- "Plan d'audit ISO 14001:2026 — vérifier la conformité climat/biodiversité"
- "Que dit le Code du Travail sénégalais sur les EPI ?"
- "Matrice de formation QHSE pour une usine agroalimentaire"
- "Procédure de gestion des déchets dangereux selon ISO 14001:2026"
