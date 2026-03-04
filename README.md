# 🎯 TaskManager Pro - Gestion de Tâches

Bienvenue dans **TaskManager Pro**, une application web moderne et élégante pour gérer vos tâches quotidiennes avec efficacité. Conçue avec une architecture propre, cette application combine la puissance de **Flask** pour le backend et une interface réactive en **Vanilla JS/CSS**.

## ✨ Fonctionnalités

- **Interface Premium** : Design moderne avec typographie Outfit, animations fluides et mode sombre subtil.
- **Gestion Complète (CRUD)** : Créez, lisez, mettez à jour et supprimez vos tâches.
- **Priorisation** : Classez vos tâches par importance (Basse, Moyenne, Haute).
- **Filtrage Intelligent** : Filtrez vos tâches par statut (Toutes, En cours, Terminées).
- **Tri Dynamique** : Triez par date de création, priorité ou échéance.
- **Persistance des Données** : Stockage sécurisé via **SQLite** et **SQLAlchemy**.
- **Validation Robuste** : Utilisation de **Pydantic** pour garantir l'intégrité des données API.

## 🛠️ Stack Technique

- **Backend** : Python 3.x, Flask
- **Base de données** : SQLite, SQLAlchemy
- **Validation** : Pydantic
- **Frontend** : HTML5, CSS3 (Vanilla), JavaScript (ES6+)
- **Architecture** : Repository Pattern (Persistence Layer)

## 🚀 Installation et Démarrage

### 1. Prérequis
Assurez-vous d'avoir Python installé sur votre machine.

### 2. Installation des dépendances
Clonez le dépôt et installez les bibliothèques nécessaires :

```bash
git clone https://github.com/Graddy12/Gestion_t-ches.git
cd Gestion_t-ches
pip install -r requirements.txt
```

### 3. Lancer l'application
Exécutez le script principal :

```bash
python main.py
```

L'application sera accessible sur `http://127.0.0.1:5000`.

## 📂 Structure du Projet

- `app/` : Cœur de l'application Flask.
  - `models.py` : Modèles de données (SQLAlchemy & Pydantic).
  - `persistence.py` : Couche d'accès aux données (Pattern Repository).
  - `routes.py` : Définition des points de terminaison de l'API.
  - `static/` : Fichiers CSS et JavaScript.
  - `templates/` : Fichiers HTML.
- `instance/` : Contient la base de données locale (ignorée par Git).
- `main.py` : Point d'entrée pour démarrer le serveur.

## 📡 API Endpoints (Documentation rapide)

| Méthode | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/tasks` | Liste toutes les tâches (supporte le tri) |
| `POST` | `/api/tasks` | Crée une nouvelle tâche |
| `GET` | `/api/tasks/<id>`| Détails d'une tâche spécifique |
| `PUT` | `/api/tasks/<id>`| Met à jour une tâche |
| `DELETE`| `/api/tasks/<id>`| Supprime une tâche |

---
Réalisé avec ❤️ pour une meilleure productivité.
