#!/usr/bin/env bash

echo "=== Installation des dépendances ==="
pip install --upgrade pip
pip install -r requirements.txt

echo "=== Collecte des fichiers statiques ==="
python manage.py collectstatic --noinput

echo "=== Création des répertoires ==="
mkdir -p logs
mkdir -p staticfiles
mkdir -p media

echo "=== Migrations ==="
python manage.py migrate --noinput

echo "=== Build terminé ==="