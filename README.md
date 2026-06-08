# Invoices-Generetor

**Invoices-Generetor** est une application web Django de gestion de factures pensée pour simplifier le travail des indépendants, petites entreprises et structures de service qui doivent créer rapidement des devis, suivre leurs clients et générer des factures propres au format PDF.

Le projet a été conçu comme une application de démonstration réaliste, utile pour un portfolio, mais aussi assez complète pour illustrer un vrai besoin métier.

## Contexte

Dans beaucoup de contextes professionnels au Cameroun, la gestion commerciale reste encore très manuelle :

- factures créées sur Excel, Word ou même à la main ;
- suivi des clients dispersé entre WhatsApp, carnets papier et fichiers locaux ;
- difficultés à retrouver l’historique des prestations ou des produits vendus ;
- manque d’un outil simple pour générer des documents propres et cohérents.

Cette application répond à ce besoin avec une interface claire et un parcours centré sur l’essentiel :

1. enregistrer des clients ;
2. organiser des catégories et des produits ;
3. créer une facture ;
4. ajouter les lignes de facture ;
5. générer un PDF directement exploitable.

## Fonctionnalités

- création et authentification d’utilisateurs ;
- tableau de bord centralisé ;
- gestion des clients ;
- gestion des catégories de produits ;
- gestion des produits ;
- création et édition de factures ;
- génération de facture au format PDF ;
- consultation des factures en attente ;
- interface simple, directe et adaptée à un usage quotidien.

## Stack technique

- **Backend** : Django 5
- **Langage** : Python
- **Base de données** : PostgreSQL
- **Authentification** : système utilisateur Django avec compte personnalisé
- **PDF** : génération HTML vers PDF avec WeasyPrint
- **Static files** : gestion des fichiers statiques via Django

## Organisation du projet

```text
Invoices-Generetor/
├── config/          # configuration principale Django
├── users/           # authentification, accueil, tableau de bord
├── customers/       # gestion des clients
├── products/        # catégories et produits
├── invoices/        # création et édition des factures
├── templates/       # templates globaux
├── static/          # fichiers CSS, images et assets
└── manage.py        # point d’entrée Django
```

## Parcours principal

Le fonctionnement attendu est le suivant :

1. l’utilisateur se connecte ou crée un compte ;
2. il ajoute ses clients ;
3. il crée ses catégories et produits ;
4. il génère une facture à partir d’un client ;
5. il ajoute les lignes de produits à la facture ;
6. il télécharge le PDF final.

## Démarrage local

Le projet peut être lancé en local avec Docker ou avec l’environnement Python habituel du projet.

### Avec Docker

```bash
docker compose up --build
```

### Avec Python

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Pages principales

- page d’accueil ;
- inscription et connexion ;
- tableau de bord ;
- liste des clients ;
- liste des catégories et produits ;
- création de facture ;
- édition de facture ;
- génération PDF.


## Notes

- Le projet utilise un compte utilisateur personnalisé.
- Les données métier sont liées entre elles : un client peut avoir plusieurs factures, et une facture contient plusieurs produits.
- Le PDF est généré directement à partir d’un template HTML, ce qui permet de conserver un rendu lisible et cohérent.

