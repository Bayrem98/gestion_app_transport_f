import os
import django
import sys

# Configuration Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transport_app.settings')
django.setup()

from django.contrib.auth.models import User
from gestion.models import Societe, HeureTransport, Agent, Chauffeur, Course

def creer_superutilisateur():
    """
    Crée un superutilisateur si aucun n'existe
    Utilise les variables d'environnement pour plus de sécurité sur Render
    """
    # Récupérer les identifiants depuis les variables d'environnement
    # (à configurer dans Render)
    admin_username = os.environ.get('ADMIN_USERNAME', 'admin')
    admin_email = os.environ.get('ADMIN_EMAIL', 'admin@transport.com')
    admin_password = os.environ.get('ADMIN_PASSWORD', None)
    
    # Vérifier si un superutilisateur existe déjà
    if User.objects.filter(is_superuser=True).exists():
        print("✅ Un superutilisateur existe déjà dans la base de données")
        for user in User.objects.filter(is_superuser=True):
            print(f"  - {user.username} ({user.email})")
        return
    
    # Créer le superutilisateur
    if admin_password:
        # Mode production (avec mot de passe depuis variables d'environnement)
        User.objects.create_superuser(
            username=admin_username,
            email=admin_email,
            password=admin_password
        )
        print(f"✅ Superutilisateur créé avec succès : {admin_username} / {admin_email}")
        print("⚠️  Mot de passe : [PROTÉGÉ - Utilisez les variables d'environnement]")
    else:
        # Mode développement (mot de passe par défaut)
        # ATTENTION: À utiliser seulement en local !
        default_password = 'admin123'
        User.objects.create_superuser(
            username='admin',
            email='admin@transport.com',
            password=default_password
        )
        print(f"✅ Superutilisateur créé avec succès : admin / {default_password}")
        print("⚠️  ATTENTION: Mode développement - Changez ce mot de passe en production !")

def creer_donnees_par_defaut():
    """
    Crée toutes les données par défaut (sociétés, agents, etc.)
    """
    # D'abord, créer le superutilisateur si nécessaire
    creer_superutilisateur()
    
    # Ensuite, créer les autres données
    print("\n=== CRÉATION DES DONNÉES PAR DÉFAUT ===")
    
    # Créer des sociétés par défaut
    societes_par_defaut = [
        {
            'nom': 'Hannibal',
            'matricule_fiscale': 'MF1238010ZAM000',
            'adresse': 'Rue rabat complexe zaoui sousse 4000',
            'telephone': '73213830',
            'email': 'compta@astragale-tunisie.com',
            'contact_personne': 'ATEF'
        },
        {
            'nom': 'ASTRAGALE',
            'matricule_fiscale': 'MF1157457DAM000',
            'adresse': 'Rue rabat complexe zaoui sousse 4000',
            'telephone': '73213830',
            'email': 'compta@astragale-tunisie.com',
            'contact_personne': 'ATEF'
        },
        {
            'nom': 'ULYSSE',
            'matricule_fiscale': 'MF1317377WAM',
            'adresse': 'Rue rabat complexe zaoui sousse 4000',
            'telephone': '73213830',
            'email': 'compta@astragale-tunisie.com',
            'contact_personne': 'ATEF'
        },
        {
            'nom': 'PENELOPE',
            'matricule_fiscale': 'MF1317388TAM',
            'adresse': 'Rue rabat complexe zaoui sousse 4000',
            'telephone': '73213830',
            'email': 'compta@astragale-tunisie.com',
            'contact_personne': 'ATEF'
        },
    ]
    
    for societe_data in societes_par_defaut:
        societe, created = Societe.objects.get_or_create(
            nom=societe_data['nom'],
            defaults=societe_data
        )
        if created:
            print(f"✅ Société créée: {societe.nom}")
        else:
            print(f"ℹ️ Société déjà existante: {societe.nom}")
    
    print("✅ Sociétés par défaut vérifiées")
    
    # Créer les heures de transport
    heures_par_defaut = [
        {'type_transport': 'ramassage', 'heure': 6, 'libelle': 'Ramassage 6h', 'ordre': 1, 'active': True},
        {'type_transport': 'ramassage', 'heure': 7, 'libelle': 'Ramassage 7h', 'ordre': 2, 'active': True},
        {'type_transport': 'ramassage', 'heure': 8, 'libelle': 'Ramassage 8h', 'ordre': 3, 'active': True},
        {'type_transport': 'ramassage', 'heure': 22, 'libelle': 'Ramassage 22h', 'ordre': 4, 'active': True},
        {'type_transport': 'depart', 'heure': 22, 'libelle': 'Départ 22h', 'ordre': 1, 'active': True},
        {'type_transport': 'depart', 'heure': 23, 'libelle': 'Départ 23h', 'ordre': 2, 'active': True},
        {'type_transport': 'depart', 'heure': 0, 'libelle': 'Départ 0h', 'ordre': 3, 'active': True},
        {'type_transport': 'depart', 'heure': 1, 'libelle': 'Départ 1h', 'ordre': 4, 'active': True},
        {'type_transport': 'depart', 'heure': 2, 'libelle': 'Départ 2h', 'ordre': 5, 'active': True},
        {'type_transport': 'depart', 'heure': 3, 'libelle': 'Départ 3h', 'ordre': 6, 'active': True},
    ]
    
    for heure_data in heures_par_defaut:
        heure, created = HeureTransport.objects.get_or_create(
            type_transport=heure_data['type_transport'],
            heure=heure_data['heure'],
            defaults={
                'libelle': heure_data['libelle'],
                'ordre': heure_data['ordre'],
                'active': heure_data['active']
            }
        )
        if created:
            print(f"✅ Heure créée: {heure}")
    
    print("✅ Heures de transport vérifiées")
    
    # ... (le reste de votre code pour les agents, chauffeurs, etc.)
    
    print("\n=== DONNÉES PAR DÉFAUT CRÉÉES AVEC SUCCÈS ===\n")
    print("📊 Résumé:")
    print(f"  - Superutilisateurs: {User.objects.filter(is_superuser=True).count()}")
    print(f"  - Sociétés: {Societe.objects.count()}")
    print(f"  - Agents: {Agent.objects.count()}")
    print(f"  - Chauffeurs: {Chauffeur.objects.count()}")
    print(f"  - Heures de transport: {HeureTransport.objects.count()}")

if __name__ == "__main__":
    creer_donnees_par_defaut()