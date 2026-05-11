# Python_Tp

## Description

Ce projet est un système de gestion de flotte spatiale développé en Python. Il permet de gérer une flotte de vaisseaux spatiaux, leurs équipages composés d'opérateurs et de mentalistes, ainsi que diverses actions comme l'ajout, la suppression, la modification et l'affichage des informations. Le système inclut également des événements aléatoires pour ajouter du dynamisme.

## Fonctionnalités

### Gestion des Vaisseaux
- Ajouter un vaisseau (marchand ou guerre)
- Supprimer un vaisseau
- Modifier le nom ou le type d'un vaisseau
- Afficher les détails des vaisseaux

### Gestion des Membres d'Équipage
- Ajouter un opérateur ou un mentaliste à un vaisseau
- Supprimer un membre d'un vaisseau
- Modifier les attributs des membres (nom, âge, genre, rôle, expérience, mana)
- Faire agir un membre (actions spécifiques selon le rôle)

### Affichages et Statistiques
- Afficher l'équipage d'un vaisseau
- Afficher les statistiques de la flotte (nombre de vaisseaux, répartition des rôles, etc.)
- Afficher la liste des vaisseaux avec leurs caractéristiques

### Autres Actions
- Vérifier la préparation d'un vaisseau
- Sauvegarder la flotte
- Charger la flotte depuis un fichier
- Événements aléatoires (attaques, tempêtes, rencontres, etc.)

### Validation des Entrées
- Vérification des genres (homme/femme)
- Vérification des âges (20-60 ans)
- Vérification des rôles (pilote, technicien, etc.)
- Vérification des types de vaisseaux (marchand/guerre)

### Événements Aléatoires
Après certaines actions (ajout, suppression, action d'un membre), il y a 20% de chance qu'un événement aléatoire se produise :
- Attaque pirate : endommage un vaisseau
- Tempête spatiale : endommage tous les vaisseaux opérationnels
- Rencontre marchande : gain d'expérience pour un marchand
- Dysfonctionnement : perte d'expérience pour un opérateur
- Bonne nouvelle : gain de mana pour un mentaliste

## Structure du Projet

```
Python_Tp/
├── main.py                 # Fichier principal avec le menu et la logique
├── classes/
│   ├── Member.py           # Classe de base pour les membres
│   ├── Operator.py         # Classe pour les opérateurs
│   ├── Mentalist.py        # Classe pour les mentalistes
│   ├── Spaceship.py        # Classe pour les vaisseaux
│   └── Fleet.py            # Classe pour la flotte
├── data.json               # Fichier de sauvegarde des données
└── README.md               # Ce fichier
```

## Classes

### Member
Classe de base pour tous les membres d'équipage.
- Attributs : first_name, last_name, gender, age
- Méthodes : introduce_yourself(), update_member()

### Operator
Hérite de Member. Représente les opérateurs techniques.
- Attributs supplémentaires : role, experience
- Méthodes : act() (action selon le rôle), gain_experience(), update_operator()

### Mentalist
Hérite de Member. Représente les mentalistes avec des pouvoirs psychiques.
- Attributs supplémentaires : mana
- Méthodes : act() (influence un opérateur), recharge_mana(), update_mentalist()

### Spaceship
Représente un vaisseau spatial.
- Attributs : name, shipType, condition, crew
- Méthodes : append_member(), remove_member(), display_crew(), check_preparation(), update_spaceship()

### Fleet
Représente la flotte de vaisseaux.
- Attributs : name, spaceships
- Méthodes : append_spaceship(), remove_spaceship(), statistics(), update_fleet()

## Installation

1. Assurez-vous d'avoir Python 3.x installé.
2. Clonez ou téléchargez le projet.
3. Exécutez `main.py` pour lancer l'application.

```bash
python main.py
```

## Utilisation

Le programme présente un menu principal avec les options suivantes :

1. **Ajouter** : Créer un vaisseau ou ajouter un membre
2. **Supprimer** : Supprimer un vaisseau ou un membre
3. **Modifier** : Modifier les attributs des vaisseaux ou membres
4. **Afficher** : Voir les équipages, statistiques ou vaisseaux
5. **Autres actions** : Vérifications, sauvegarde, chargement, actions des membres

Suivez les invites pour naviguer dans les menus. Les données sont automatiquement sauvegardées après chaque action modifiant l'état.

## Rôles des Opérateurs

- **Pilote** : S'entraîne sur un simulateur
- **Technicien** : Nettoie le vaisseau (ou répare s'il est endommagé)
- **Commandant** : Fait des vérifications
- **Armurier** : Fabrique une arme
- **Marchand** : Surveille son stock
- **Entretien** : Effectue la maintenance du vaisseau

## Préparation d'un Vaisseau

Un vaisseau est considéré comme prêt s'il a :
- Au moins un pilote
- Au moins un technicien
- Au moins un mentaliste avec un mana ≥ 50

## Sauvegarde

Les données sont sauvegardées automatiquement dans `data.json` après chaque modification. Le fichier peut être rechargé au démarrage.

## Événements

Les événements aléatoires ajoutent de l'imprévisibilité. Ils peuvent améliorer ou détériorer l'état de la flotte, encourageant une gestion stratégique.

## Auteur

Alexane


