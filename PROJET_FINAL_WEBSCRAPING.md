# Projet de Fin de Module — Web Scraping
## Pipeline de WebScraping, Nettoyage et Stockage avec Dockerisation et Monitoring

**Enseignant :** Dr N'golo Konate  
**Institution :** ENSEA — AS Data Science  
**Durée :** 6 semaines  
**Modalité :** Projet en groupe (3-4 étudiants)

---

## Contexte et Objectifs

### Contexte

Dans le cadre de l'automatisation et de la gestion des données sur le web, ce projet vise à concevoir et implémenter un **pipeline complet de production** permettant :

- La collecte automatisée de données depuis un site web (web scraping)
- Le nettoyage et la structuration des données
- Le stockage dans une base de données pour exploitation ultérieure
- L'exposition des données via une API REST
- La gestion des tâches asynchrones et planifiées
- La conteneurisation complète avec Docker
- Le monitoring des performances (niveau avancé)

### Objectifs Pédagogiques

À l'issue de ce projet, vous serez capables de :

1. **Concevoir** une architecture complète de pipeline de données
2. **Implémenter** un système de scraping robuste et éthique
3. **Développer** une API REST professionnelle
4. **Conteneuriser** une application multi-services avec Docker
5. **Automatiser** des tâches récurrentes avec un gestionnaire de tâches
6. **Documenter** et **présenter** votre travail de manière professionnelle
7. **Collaborer** efficacement en équipe avec Git/GitHub

---

## Organisation du Projet

### Constitution des Équipes

- **Taille :** 2 étudiants par groupe (1 groupe de 3 exceptionnellement)
- **Rôles suggérés :**
  - Data Engineer (scraping + nettoyage)
  - Backend Developer (API + base de données)
  - DevOps Engineer (Docker + Celery + monitoring)

### Repository GitHub — OBLIGATOIRE

**Chaque groupe DOIT :**

1. Créer un repository GitHub (public ou privé)
2. Inviter l'enseignant comme collaborateur : **`ingngolo@gmail.com`**
3. Commits réguliers : minimum 2 commits/semaine/membre
4. Structure de projet professionnelle dès le début

**Nom suggéré du repository :**  
`webscraping-pipeline-[nom-groupe]`

---

##  Niveaux d'Évaluation — Système Bronze / Argent / Or

Le projet est évalué selon **3 niveaux de réalisation**. Chaque groupe choisit son niveau d'ambition.

###  Niveau BRONZE — Note Maximum : 12/20

**Pipeline fonctionnel de base**

**Fonctionnalités obligatoires :**

1.  **Web Scraping**
   - Script Python avec BeautifulSoup ou Scrapy
   - Extraction d'au moins 50 éléments
   - Respect de `robots.txt` et délai entre requêtes
   - Gestion basique des erreurs

2.  **Nettoyage des Données**
   - Fonction de nettoyage avec pandas
   - Suppression des doublons
   - Traitement des valeurs manquantes
   - Standardisation des formats

3.  **Stockage**
   - Base de données SQLite ou PostgreSQL
   - Schéma défini
   - Insertion des données nettoyées

4.  **API REST Basique (Flask)**
   - `GET /data` : Récupérer toutes les données
   - `GET /data/{id}` : Récupérer un élément
   - `POST /scrape` : Lancer le scraping
   - Réponses JSON structurées

**Technologies :**
- Python 3.10+
- BeautifulSoup ou Scrapy
- Flask
- SQLite ou PostgreSQL
- pandas

---

###  Niveau ARGENT — Note Maximum : 16/20

**Pipeline dockerisé avec automatisation**

**Tout le Niveau Bronze + :**

5.  **Dockerisation**
   - Dockerfile pour l'application
   - docker-compose.yml orchestrant :
     - Service API (Flask)
     - Service Base de données (PostgreSQL)
   - Volumes Docker pour persistance
   - Variables d'environnement (.env)

6.  **Gestion des Tâches Asynchrones (Celery)**
   - Celery configuré avec Redis
   - Tâche Celery pour le scraping
   - Endpoint `POST /scrape/async`
   - Vérification du statut des tâches

7.  **API REST Améliorée**
   - Pagination : `GET /data?page=1&limit=10`
   - Recherche : `GET /data/search?query=...`
   - Gestion d'erreurs HTTP (404, 500, etc.)

**Technologies supplémentaires :**
- Docker & Docker Compose
- Celery
- Redis
- PostgreSQL (obligatoire)

---

###  Niveau OR — Note Maximum : 20/20

**Pipeline de production avec monitoring**

**Tout le Niveau Argent + :**

8.  **Planification Automatique (Celery Beat)**
   - Celery Beat configuré
   - Scraping automatique périodique
   - Logs des exécutions

9.  **Monitoring et Observabilité**
   - **Option A :** Prometheus + Grafana
   - **Option B :** Logging avancé + ELK Stack
   - **Option C :** Alternative justifiée
   - Au moins 1 dashboard fonctionnel

10.  **Qualité et Robustesse**
    - Tests unitaires (pytest) pour ≥3 fonctions
    - Gestion avancée des erreurs
    - Documentation API complète (Swagger/OpenAPI)

11.  **Features Avancées** (au moins 1) :
    - GraphQL au lieu de REST
    - Frontend web simple
    - Scraping de sites complexes
    - Export des données (CSV, Excel, PDF)
    - Système de notification

**Technologies supplémentaires :**
- Celery Beat
- Prometheus + Grafana OU alternative
- pytest
- Swagger/OpenAPI

---

##  Sites Autorisés pour le Scraping

###  RÈGLES ÉTHIQUES — OBLIGATOIRES

1. Vérifier `robots.txt`
2. Respecter les délais (≥1 seconde entre requêtes)
3. User-Agent identifiable : "ENSEA Educational Project"
4. Pas de données personnelles
5. Limiter le volume (max 500 items)

###  Sites Pré-Validés

**E-Commerce Côte d'Ivoire :**
-  Jumia CI (vérifier robots.txt, limiter à 50 produits)
-  Cdiscount (vérifier robots.txt)

**Actualités :**
-  Fratmat.info (vérifier robots.txt)
-  Abidjan.net (privilégier RSS si disponible)

**Emploi :**
-  Emploi.ci
-  ReKrute (vérifier robots.txt)

**APIs Publiques (Alternative) :**
-  GitHub API
-  OpenWeatherMap API
-  PokeAPI
-  JSONPlaceholder

###  Sites INTERDITS

-  Réseaux sociaux (Facebook, Twitter, LinkedIn)
-  Amazon
-  Google Search Results
-  Sites nécessitant authentification
-  Sites avec anti-bot agressif (Cloudflare)

###  Validation Obligatoire

**Avant de commencer :** Envoyer un email à `konatengolo@ufhb.edu.ci` regroupaant tout les groupes avec :
- Nom du groupe (membre)
- Site choisi
- Capture de `robots.txt`
- Justification du choix (Pertinance du projet dans l'ecosysteme numerique)

**Délai de validation :** 48h

---

##  Livrables et Échéances

### Planning Global (6 Semaines)

| Semaine | Phases | Jalons |
|---------|--------|--------|
| **1** | Scraping | Script + 50 items |
| **1** | Nettoyage + DB | Données en base |
| **2** | API REST | API opérationnelle |
| **2** | Docker | docker-compose up |
| **3** | Celery (+Beat) | Tasks async |
| **3** | Monitoring + Finitions | Dashboard + Soutenance |

### 📍 Jalon 1 — Semaine 1

**Livrable :** Scraping + Nettoyage

-  Repository GitHub créé et accès donné
-  Script de scraping fonctionnel
-  Fichier `raw_data.json` (≥50 items)
-  Module de nettoyage
-  README.md à jour

**Poids :** 10% de la note finale

---

###  Jalon 2 — Semaine 2 

**Livrable :** Base de Données + API

**Niveau Bronze :**
-  BD avec ≥50 enregistrements
-  API Flask (3 endpoints)
-  Documentation API

**Niveau Argent/Or :**
-  Tout Bronze +
-  Docker Compose fonctionnel
-  `docker-compose up` démarre tous services

**Poids :** 20% de la note finale

---

###  Livrable Final — Semaine 3 (Vendredi 23h59)

**Tous niveaux :**

-  Code complet sur GitHub
-  README professionnel avec :
  - Description du projet
  - Membres et rôles
  - Technologies utilisées
  - Instructions d'installation
  - Captures d'écran
  - Badge du niveau visé
-  Documentation technique complète
-  Vidéo de démo (3-5 min) — **OBLIGATOIRE**

**Spécifique par niveau :**

**Bronze :**
-  Pipeline complet (scraping → API)

**Argent :**
-  Tout Bronze + Docker + Celery

**Or :**
- Tout Argent + Celery Beat + Monitoring + Tests

**Poids :** 50% de la note finale

---

###  Soutenance Finale — Semaine 7

**Durée :** 20 minutes (15 min présentation + 5 min questions)

**Déroulement :**

1. Présentation du projet (5 min)
2. Démonstration live (8 min)
3. Aspects techniques (2 min)
4. Questions du jury (5 min)

**Poids :** 20% de la note finale

---

##  Critères d'Évaluation

### Grille de Notation Globale

| Critère | Poids |
|---------|-------|
| Jalons Intermédiaires | 30% |
| Livrable Final | 50% |
| Soutenance | 20% |

### Bonus (+2 points max)

- +0.5 : Vidéo de démo exceptionnelle
- +0.5 : CI/CD avec GitHub Actions
- +0.5 : Tests avec couverture >80%
- +0.5 : Documentation Sphinx/MkDocs
- +1 : Feature très originale

### Pénalités

- -2 : Retard livrable final (par jour)
- -3 : Scraping d'un site interdit
- -5 : Plagiat détecté
- -10 : Non-respect éthique grave
- 0 : Projet non démarrable

### Contribution Individuelle

**Modulation de note :** ±20% selon :
- Commits GitHub
- Réponses aux questions (soutenance)
- Autoévaluation par les pairs

---

##  Technologies Recommandées

| Composant | Recommandé | Alternatives |
|-----------|------------|--------------|
| Scraping | Scrapy, BeautifulSoup | Selenium |
| API | Flask | Django REST, FastAPI |
| Base de données | PostgreSQL | MongoDB, SQLite (Bronze) |
| Async Tasks | Celery + Redis | RQ, Dramatiq |
| Conteneurisation | Docker Compose | - |
| Monitoring | Prometheus + Grafana | ELK Stack |

**Vous pouvez choisir d'autres technologies si vous justifiez ce choix dans votre documentation.**

---

##  Charte Éthique et Légale

En participant à ce projet, je m'engage à :

1.  Respecter les robots.txt
2.  Limiter le volume de requêtes (max 500 items)
3.  Identifier mon scraper (User-Agent explicite)
4.  Ne pas scraper de données personnelles
5.  Valider mon site auprès de l'enseignant
6.  Citer mes sources
7.  Ne pas plagier
8.  Contribuer équitablement
9.  Respecter les délais
10.  Être honnête en cas de difficulté



---

##  Support

### Office Hours

- **Quand :** Office hours (hypothetiquement)
- **Format :** Questions techniques, debugging, revue de code

### Contact

- **Email :** konatengolo@ufhb.edu.ci
- **GitHub :** Mentionner `@nKonate` (ou `@muss2kn`) dans vos Issues
- **Délai de réponse :** 48h max

---

##  Checklist de Validation Finale

**Avant de rendre :**

### Code
- [ ] Scraper fonctionne et respecte l'éthique
- [ ] Données nettoyées et en base
- [ ] API REST opérationnelle
- [ ] Docker Compose démarre (Argent/Or)
- [ ] Celery opérationnel (Argent/Or)
- [ ] Monitoring fonctionnel (Or)

### Documentation
- [ ] README complet
- [ ] INSTALLATION.md
- [ ] API_DOCUMENTATION.md
- [ ] ARCHITECTURE.md
- [ ] CHARTE_SIGNEE.pdf
- [ ] Captures d'écran

### GitHub
- [ ] Accès donné à `ingngolo@gmail.com`
- [ ] Commits réguliers
- [ ] .gitignore configuré
- [ ] Niveau visé indiqué

### Livrable
- [ ] Vidéo de démo (3-5 min) (fortement recommandé mais sanctionné si non effectué)
- [ ] Présentation préparée
- [ ] Chaque membre maîtrise sa partie

---

##  Conseils pour Réussir

1. **Commencer tôt** — Ne pas attendre la dernière semaine
2. **Communiquer** — Réunion hebdomadaire minimum
3. **Documenter** — Au fur et à mesure, pas à la fin
4. **Tester** — Chaque phase avant de continuer
5. **Demander de l'aide** — Ne pas rester bloqué >2 jours
6. **Viser réaliste** — Bronze parfait > Or bancal

---

##  Contact

**Enseignant :** Dr N'golo Konate  
**Email :** konatengolo@ufhb.edu.ci  
**Office Hours :** mardi 12h-14h

---

**Bon courage ! **

**Chaque projet realisé est une opportunité exceptionnelle de développer des compétences professionnelles très demandées. Faites-en des fleurons de votre portfolio !**
