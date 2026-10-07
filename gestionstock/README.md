# Gestion de stock de tissus

Application web Django pour gérer le stock d'un vendeur de tissus.

## Fonctionnalités
- Liste des tissus (type, couleur, largeur, prix au mètre, métrage en stock)
- Alerte visuelle quand le stock est bas
- Recherche par nom, couleur ou référence
- Ajout et retrait de métrage depuis la page
- Connexion sécurisée
- Espace d'administration

## Technologies
Python, Django, SQLite, HTML/CSS

## Installation
    python -m venv env
    source env/Scripts/activate
    pip install django
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver