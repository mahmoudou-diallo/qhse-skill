---
title: Outils QHSE Open-Source
description: Catalogue d'outils logiciels open-source pour le management QHSE
---

# Outils QHSE — Catalogue Open-Source

## Plateformes HSE complètes

### BeaconHS
- **Description** : Plateforme HSE multi-tenant open-source pour construction industrielle
- **Techno** : Next.js 16 / React 19 / Drizzle / PostgreSQL
- **Modules** : Incidents, JSHA/HazID, inspections, formation, équipements, PPE, documents, CAPA
- **Form builder** : Moteur de formulaires avec logique conditionnelle
- **Licence** : Open-source
- **GitHub** : https://github.com/braedonsaunders/beaconhs
- **Cas d'usage** : PME/ETI, chantiers, suivi HSE complet

### Autonomous EHS
- **Description** : Console EHS autonome : incidents, CAPA, audits, PostgreSQL
- **Techno** : TypeScript / PostgreSQL / Drizzle
- **Modules** : Incidents, CAPA, audits, intégrations, RAG IA optionnel
- **Particularité** : RBAC, escalade automatique, TRIR analytics
- **Licence** : Apache 2.0
- **GitHub** : https://github.com/SafetyMP/Autonomous-EHS-Management
- **Cas d'usage** : Conformité, reporting, traçabilité

### Odin
- **Description** : Application desktop EHS pour petites manufactures
- **Techno** : Go + React + SQLite
- **Modules** : Établissements, employés, produits chimiques, incidents, inspections, permis, PPE, formation, déchets
- **Particularité** : Applicatif local (pas de SaaS), piste d'audit git
- **Licence** : Open-source
- **GitHub** : https://github.com/asgardehs/odin
- **Cas d'usage** : PMI manufacturières, données en local

## Outils spécialisés

### HSE Digital Toolkit (UmairPashaa)
- **Description** : PWA mobile offline pour HSE terrain
- **Techno** : PWA, HTML/CSS/JS
- **Modules** : Risk Assessment, PPE checklist, Incident Report, Safety Inspection
- **Premium** : JSA, CAPA, Audit, HSE Objectives, Meeting Minutes
- **Standards** : Saudi Aramco SSMS, OSHA, ISO 45001
- **Inclus** : Cours NEBOSH, IOSH, OSHA, Q&A entretien HSE
- **Licence** : Open-source
- **GitHub** : https://github.com/UmairPashaa/HSE-Digital-Toolkit
- **Cas d'usage** : Terrain, zones sans connexion, inspections mobiles

### HSE-AI Insight Platform
- **Description** : Plateforme IA pour analyse incidents HSE Oil & Gas
- **Techno** : NestJS + Next.js + PostgreSQL + RabbitMQ + OpenSearch + Ollama
- **Fonctionnalité** : Extraction structurée de rapports en texte libre via LLM local
- **Dashboard** : KPIs, tendances, tags, classification
- **Licence** : Open-source
- **GitHub** : https://github.com/fredericoahb/hse-ai-insight-platform
- **Cas d'usage** : Analyse incidents, extraction données non structurées

### HSEI Platform (NinaHenchy)
- **Description** : Analytics HSE pour Oil & Gas (incidents + process safety)
- **Techno** : Python + Streamlit + SQLite + Docker
- **Standards** : API RP 754, ISO 45001, OSHA, RIDDOR, NUPRC
- **Modules** : Incident Register, Process Safety, CAPA, Leading Indicators, PTW, Training
- **KPIs** : TRIR, LTIR, Near Miss Ratio, Action Close-out
- **Licence** : Open-source
- **GitHub** : https://github.com/NinaHenchy/hsei-platform
- **Cas d'usage** : Analysis, reporting, dashboards Oil & Gas

### KUREAS
- **Description** : Suite de modules analyse fiabilité et risques (PRA)
- **Techno** : HTML standalone (pas de serveur, pas d'installation)
- **Modules** : Hazard Analysis, Fault Tree, Event Tree, System Modeling, FMEA
- **Standards** : SAPHIRE INL, NUREG-7039, OpenPSA
- **Licence** : Open-source
- **GitHub** : https://github.com/curtlsmith/KUREAS
- **Cas d'usage** : Analyse de risques probabiliste, ingénierie fiabilité

### InspectionPress
- **Description** : OS complet pour inspections terrain
- **Techno** : Full-stack, PWA, AWS/Twilio/SES
- **Modules** : Scheduling, templates, CRM, rapports PDF, media capture
- **Particularité** : Formulaires personnalisés, génération rapports PDF
- **Licence** : GPL
- **GitHub** : https://github.com/inspectionpress/inspection.press
- **Cas d'usage** : Inspections terrain, rapports, CRM

### SmartQHSE
- **Description** : Plateforme IA multi-ISO (pas open-source mais référence)
- **Standards** : ISO 9001, 14001, 45001
- **Modules** : Conformité, incidents, inspections, risques, audits
- **Couverture** : Afrique Ouest (Nigeria, Ghana, Sénégal, Côte d'Ivoire)
- **Site** : https://www.smartqhse.com
- **Cas d'usage** : Conformité multi-pays Afrique Ouest

## Sélection par besoin

| Besoin | Outil recommandé |
|---|---|
| Suivi HSE complet (PME) | BeaconHS |
| Inspection terrain offline | HSE Digital Toolkit |
| Analyse incidents IA | HSE-AI Insight Platform |
| Conformité PMI | Odin |
| Dashboard Oil & Gas | HSEI Platform |
| Analyse risques probabiliste | KUREAS |
| Inspections + CRM | InspectionPress |
| Conformité Sénégal/Afrique Ouest | SmartQHSE |
