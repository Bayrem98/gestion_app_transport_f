#!/usr/bin/env bash
# Script de build pour Render

# Installer les dépendances Python
pip install -r requirements.txt

# Créer les répertoires nécessaires
mkdir -p staticfiles
mkdir -p media
mkdir -p logs

# Collecter les fichiers statiques
python manage.py collectstatic --noinput

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur par défaut (optionnel)
# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell