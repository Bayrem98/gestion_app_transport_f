#!/usr/bin/env bash

echo "=== Installation des dépendances ==="
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo "=== Vérification de l'installation ==="
python -c "import django; print(f'Django version: {django.get_version()}')"

echo "=== Collecte des fichiers statiques ==="
python manage.py collectstatic --noinput

echo "=== Création des répertoires ==="
mkdir -p logs
mkdir -p staticfiles
mkdir -p media

echo "=== Migrations ==="
python manage.py migrate --noinput

echo "=== Build terminé ==="