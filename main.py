from classes.Member import *
from classes.Operator import *
from classes.Mentalist import *
from classes.Spaceship import *
from classes.Fleet import *
import json, random

def trigger_random_event(fleet):
    if random.randint(1, 5) == 1:
        event_num = random.randint(1, 5)
        if event_num == 1:
            operational_ships = [s for s in fleet.spaceships if s.condition.lower() == "opérationnel"]
            if operational_ships:
                ship = random.choice(operational_ships)
                ship.condition = "endommagé"
                print(f"Événement aléatoire : Attaque pirate ! Le vaisseau {ship.name} est endommagé.")
                save_data(fleet)
        elif event_num == 2:
            for s in fleet.spaceships:
                if s.condition.lower() == "opérationnel":
                    s.condition = "endommagé"
            print("Événement aléatoire : Tempête spatiale ! Tous les vaisseaux opérationnels sont endommagés.")
            save_data(fleet)
        elif event_num == 3:
            marchands = [m for s in fleet.spaceships for m in s.crew if isinstance(m, Operator) and m.role == "marchand"]
            if marchands:
                marchand = random.choice(marchands)
                marchand.experience += 1
                print(f"Événement aléatoire : Rencontre marchande ! {marchand.first_name} {marchand.last_name} gagne 1 point d'expérience.")
                save_data(fleet)
        elif event_num == 4:
            operators = [m for s in fleet.spaceships for m in s.crew if isinstance(m, Operator)]
            if operators:
                op = random.choice(operators)
                if op.experience > 0:
                    op.experience -= 1
                    print(f"Événement aléatoire : Dysfonctionnement technique ! {op.first_name} {op.last_name} perd 1 point d'expérience.")
                    save_data(fleet)
        elif event_num == 5:
            mentalists = [m for s in fleet.spaceships for m in s.crew if isinstance(m, Mentalist)]
            if mentalists:
                mentalist = random.choice(mentalists)
                mentalist.mana = min(100, mentalist.mana + 10)
                print(f"Événement aléatoire : Bonne nouvelle ! {mentalist.first_name} {mentalist.last_name} gagne 10 points de mana.")
                save_data(fleet)

def save_data(fleet, file_name="data.json"):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(fleet, file, default=custom_serializer, indent=4, ensure_ascii=False)
    print("Flotte sauvegardée")


def custom_serializer(obj):
    if isinstance(obj, Spaceship):
        return {
            "_name": obj.name,
            "_shipType": obj.shipType,
            "_condition": obj.condition,
            "_crew": obj.crew,
        }
    if isinstance(obj, Fleet):
        return {
            "_name": obj.name,
            "_spaceships": obj.spaceships
        }
    return obj.__dict__

def load_data(file_name="data.json"):
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
    fleet_name = data.get("_name", "Galactica")
    fleet = Fleet(fleet_name)

    for ship_data in data.get("_spaceships", []):
        ship = Spaceship(ship_data.get("_name", "Unknown"), ship_data.get("_shipType", "marchand"))
        ship.condition = ship_data.get("_condition", "opérationnel")

        for member_data in ship_data.get("_crew", []):
            first_name = member_data.get("_first_name")
            last_name = member_data.get("_last_name")
            gender = member_data.get("_gender")
            age = member_data.get("_age")

            if "_role" in member_data:
                role = member_data.get("_role")
                experience = member_data.get("_experience", 0)
                crew_member = Operator(first_name, last_name, gender, age, role)
                crew_member.experience = experience
            else:
                mana = member_data.get("_mana", 0)
                crew_member = Mentalist(first_name, last_name, gender, age, mana)

            ship.append_member(crew_member)

        fleet.append_spaceship(ship)
    print("\nFlotte chargée")
    return fleet

try:
    fleet = load_data("data.json")
except FileNotFoundError:
    print("Aucun fichier data.json trouvé. Création d'une flotte vide.")
    fleet = Fleet("Galactica")

# === Menu principal ===
while True:
    print("\n=== MENU PRINCIPAL ===")
    print("Que voulez-vous faire ?")
    print("1. Ajouter")
    print("2. Supprimer")
    print("3. Modifier")
    print("4. Afficher")
    print("5. Autres actions")
    print("0. Quitter\n")
    choice = input("Votre choix : ")

    match choice:
        case "1":  # Ajouter
            print("\n=== AJOUTER ===")
            print("1. Créer un vaisseau")
            print("2. Ajouter un membre à un vaisseau\n")
            sub_choice = input("Votre choix : ")
            match sub_choice:
                case "1":
                    ship_name = input("\nNom du vaisseau : ")
                    ship_type = input("Type du vaisseau (marchand/guerre) : ").strip().lower()
                    valid_types = ["marchand", "guerre"]
                    while ship_type not in valid_types:
                        print("Type invalide. Veuillez entrer 'marchand' ou 'guerre'.")
                        ship_type = input("Type du vaisseau (marchand/guerre) : ").strip().lower()
                    ship = Spaceship(ship_name, ship_type)
                    fleet.append_spaceship(ship)
                    print(f"Le vaisseau {ship.name} a été ajouté dans la flotte {fleet.name}")
                    save_data(fleet)
                    trigger_random_event(fleet)
                case "2":
                    ship_name = input("\nNom du vaisseau : ").strip().lower()
                    found = False
                    for ship in fleet.spaceships:
                        if ship.name.lower() == ship_name:
                            print("Type de membre à ajouter :")
                            print("1. Opérateur")
                            print("2. Mentaliste\n")
                            choix = input("Votre choix : ")

                            first_name = input("\nPrénom : ")
                            last_name = input("Nom : ")
                            gender = input("Genre (homme/femme) : ").strip().lower()
                            while gender not in ["homme", "femme"]:
                                print("Genre invalide. Veuillez entrer 'homme' ou 'femme'.")
                                gender = input("Genre (homme/femme) : ").strip().lower()
                            while True:
                                try:
                                    age = int(input("Âge : "))
                                    if 20 <= age <= 60:
                                        break
                                    else:
                                        print("Âge invalide. L'âge doit être entre 20 et 60 ans.")
                                except ValueError:
                                    print("Veuillez entrer un nombre entier pour l'âge.")
                            match choix :
                                case "1" :
                                    role = input("Rôle (pilote/technicien/commandant/armurier/entretien/marchand) : ").strip().lower()
                                    valid_roles = ["pilote", "technicien", "commandant", "armurier", "entretien", "marchand"]
                                    while role not in valid_roles:
                                        print("Rôle invalide. Veuillez choisir parmi : pilote, technicien, commandant, armurier, entretien, marchand")
                                        role = input("Rôle (pilote/technicien/commandant/armurier/entretien/marchand) : ").strip().lower()
                                    experience = int(input("Expérience (années) : "))
                                    crew_member = Operator(first_name, last_name, gender, age, role)
                                    crew_member.experience = experience
                                case "2":
                                    mana = int(input("Mana (max 100) : "))
                                    if mana > 100:
                                        mana = 100 
                                        print("Le mana ne peut pas dépasser 100, valeur fixée à 100.")
                                    elif mana < 0:
                                        mana = 0 
                                        print("Le mana ne peut pas être négatif, valeur fixée à 0.")

                                    crew_member = Mentalist(first_name, last_name, gender, age, mana)
                                case _:
                                    print("Choix invalide, membre non ajouté.")
                                    break
                            ship.append_member(crew_member)
                            print(f"{crew_member.first_name} {crew_member.last_name} à été ajouté à l'équipage du vaisseau {ship.name}")
                            save_data(fleet)
                            trigger_random_event(fleet)
                            found = True
                            break
                    if not found:
                        print(f"Aucun vaisseau nommé {ship_name} n'a été trouvé.")
                case _:
                    print("Choix invalide.")

        case "2":  # Supprimer
            print("\n=== SUPPRIMER ===")
            print("1. Supprimer un vaisseau")
            print("2. Supprimer un membre d'un vaisseau\n")
            sub_choice = input("Votre choix : ")
            match sub_choice:
                case "1":
                    ship_name = input("\nNom du vaisseau à supprimer : ").strip().lower()
                    if fleet.remove_spaceship(ship_name):
                        save_data(fleet)
                        trigger_random_event(fleet)
                case "2":
                    ship_name = input("\nNom du vaisseau : ").strip().lower()
                    last_name = input("Nom du membre à supprimer : ").strip().lower()
                    found = False
                    for ship in fleet.spaceships:
                        if ship.name.lower() == ship_name:
                            ship.remove_member(last_name)
                            save_data(fleet)
                            trigger_random_event(fleet)
                            found = True
                            break
                    if not found:
                        print(f"Aucun vaisseau nommé {ship_name} n'a été trouvé.")
                case _:
                    print("Choix invalide.")

        case "3":  # Modifier
            print("\n=== MODIFIER ===")
            print("1. Modifier un vaisseau")
            print("2. Modifier la flotte")
            print("3. Modifier un membre d'un vaisseau\n")
            sub_choice = input("Votre choix : ")
            match sub_choice:
                case "1":
                    ship_name = input("\nNom du vaisseau à modifier : ").strip().lower()
                    found = False
                    for ship in fleet.spaceships:
                        if ship.name.lower() == ship_name:
                            print("Que voulez-vous modifier ?")
                            print("1. Nom")
                            print("2. Type")
                            print("3. Condition\n")
                            sub_sub_choice = input("Votre choix : ")
                            match sub_sub_choice:
                                case "1":
                                    new_name = input("\nNouveau nom : ")
                                    ship.update_spaceship(name=new_name)
                                case "2":
                                    new_type = input("\nNouveau type (marchand/guerre) : ")
                                    ship.update_spaceship(shipType=new_type)
                                case "3":
                                    new_condition = input("\nNouvelle condition : ")
                                    ship.update_spaceship(condition=new_condition)
                                case _:
                                    print("\nChoix invalide.")
                            save_data(fleet)
                            found = True
                            break
                    if not found:
                        print(f"Aucun vaisseau nommé {ship_name} n'a été trouvé.")
                case "2":
                    new_fleet_name = input("\nNouveau nom de la flotte : ")
                    fleet.update_fleet(name=new_fleet_name)
                    save_data(fleet)
                case "3":
                    ship_name = input("\nNom du vaisseau : ").strip().lower()
                    last_name = input("Nom du membre à modifier : ").strip().lower()
                    found = False
                    for ship in fleet.spaceships:
                        if ship.name.lower() == ship_name:
                            for member in ship.crew:
                                if member.last_name.lower() == last_name:
                                    print("Que voulez-vous modifier ?")
                                    print("1. Prénom")
                                    print("2. Nom")
                                    print("3. Genre")
                                    print("4. Âge")
                                    if isinstance(member, Operator):
                                        print("5. Rôle")
                                        print("6. Expérience\n")
                                        sub_sub_choice = input("Votre choix : ")
                                        match sub_sub_choice:
                                            case "1":
                                                new_first = input("\nNouveau prénom : ")
                                                member.update_operator(first_name=new_first)
                                            case "2":
                                                new_last = input("\nNouveau nom : ")
                                                member.update_operator(last_name=new_last)
                                            case "3":
                                                new_gender = input("\nNouveau genre (homme/femme) : ").strip().lower()
                                                while new_gender not in ["homme", "femme"]:
                                                    print("Genre invalide. Veuillez entrer 'homme' ou 'femme'.")
                                                    new_gender = input("Nouveau genre (homme/femme) : ").strip().lower()
                                                member.update_operator(gender=new_gender)
                                            case "4":
                                                while True:
                                                    try:
                                                        new_age = int(input("\nNouvel âge : "))
                                                        if 20 <= new_age <= 60:
                                                            break
                                                        else:
                                                            print("Âge invalide. L'âge doit être entre 20 et 60 ans.")
                                                    except ValueError:
                                                        print("Veuillez entrer un nombre entier pour l'âge.")
                                                member.update_operator(age=new_age)
                                            case "5":
                                                new_role = input("\nNouveau rôle (pilote/technicien/commandant/armurier/entretien/marchand) : ").strip().lower()
                                                valid_roles = ["pilote", "technicien", "commandant", "armurier", "entretien", "marchand"]
                                                while new_role not in valid_roles:
                                                    print("Rôle invalide. Veuillez choisir parmi : pilote, technicien, commandant, armurier, entretien, marchand")
                                                    new_role = input("Nouveau rôle (pilote/technicien/commandant/armurier/entretien/marchand) : ").strip().lower()
                                                member.update_operator(role=new_role)
                                            case "6":
                                                new_exp = int(input("\nNouvelle expérience : "))
                                                member.update_operator(experience=new_exp)
                                            case _:
                                                print("\nChoix invalide.")
                                    elif isinstance(member, Mentalist):
                                        print("5. Mana\n")
                                        sub_sub_choice = input("Votre choix : ")
                                        match sub_sub_choice:
                                            case "1":
                                                new_first = input("\nNouveau prénom : ")
                                                member.update_mentalist(first_name=new_first)
                                            case "2":
                                                new_last = input("\nNouveau nom : ")
                                                member.update_mentalist(last_name=new_last)
                                            case "3":
                                                new_gender = input("\nNouveau genre (homme/femme) : ").strip().lower()
                                                while new_gender not in ["homme", "femme"]:
                                                    print("Genre invalide. Veuillez entrer 'homme' ou 'femme'.")
                                                    new_gender = input("Nouveau genre (homme/femme) : ").strip().lower()
                                                member.update_mentalist(gender=new_gender)
                                            case "4":
                                                while True:
                                                    try:
                                                        new_age = int(input("\nNouvel âge : "))
                                                        if 20 <= new_age <= 60:
                                                            break
                                                        else:
                                                            print("Âge invalide. L'âge doit être entre 20 et 60 ans.")
                                                    except ValueError:
                                                        print("Veuillez entrer un nombre entier pour l'âge.")
                                                member.update_mentalist(age=new_age)
                                            case "5":
                                                new_mana = int(input("\nNouveau mana (0-100) : "))
                                                member.update_mentalist(mana=new_mana)
                                            case _:
                                                print("\nChoix invalide.")
                                    save_data(fleet)
                                    found = True
                                    break
                            if found:
                                break
                    if not found:
                        print(f"Aucun membre nommé {last_name} n'a été trouvé dans le vaisseau {ship_name}.")
                case _:
                    print("\nChoix invalide.")

        case "4":  # Afficher
            print("\n=== AFFICHER ===")
            print("1. Afficher l'équipage d'un vaisseau")
            print("2. Afficher les statistiques de la flotte")
            print("3. Afficher la flotte\n")
            sub_choice = input("Votre choix : ")
            match sub_choice:
                case "1":
                    ship_name = input("\nNom du vaisseau : ").strip().lower()
                    found = False
                    for ship in fleet.spaceships:
                        if ship.name.lower() == ship_name:
                            ship.display_crew()
                            found = True
                            break
                    if not found:
                        print(f"Aucun vaisseau nommé {ship_name} n'a été trouvé.")
                case "2":
                    fleet.statistics()
                case "3":
                    for ship in fleet.spaceships:
                        ship.display_crew()
                case _:
                    print("\nChoix invalide.")

        case "5":  # Autres actions
            print("\n=== AUTRES ACTIONS ===")
            print("1. Vérifier la préparation d'un vaisseau")
            print("2. Sauvegarder la flotte")
            print("3. Charger la flotte")
            print("4. Faire agir un membre\n")
            sub_choice = input("Votre choix : ")
            match sub_choice:
                case "1":
                    ship_name = input("\nNom du vaisseau : ").strip().lower()
                    found = False
                    for ship in fleet.spaceships:
                        if ship.name.lower() == ship_name:
                            if ship.check_preparation():
                                print("Le vaisseau est prêt !")
                            else:
                                print("Le vaisseau n'est pas prêt.")
                            trigger_random_event(fleet)
                            found = True
                            break
                    if not found:
                        print(f"Aucun vaisseau nommé {ship_name} n'a été trouvé.")
                case "2":
                    save_data(fleet, "data.json")
                case "3":
                    try:
                        fleet = load_data("data.json")
                    except FileNotFoundError:
                        print("\nLe fichier est introuvable.")
                case "4":
                    ship_name = input("\nNom du vaisseau : ").strip().lower()
                    found = False
                    for ship in fleet.spaceships:
                        if ship.name.lower() == ship_name:
                            member_name = input("Nom du membre : ").strip().lower()
                            for member in ship.crew:
                                if member.last_name.lower() == member_name:
                                    if isinstance(member, Operator):
                                        if member.role == "technicien" and ship.condition.lower() != "opérationnel":
                                            ship.condition = "opérationnel"
                                            print(member.first_name, member.last_name, "répare le vaisseau", ship.name)
                                            save_data(fleet)
                                        else:
                                            member.act()
                                    elif isinstance(member, Mentalist):
                                        operator_name = input("Nom de l'opérateur à influencer : ").strip().lower()
                                        for op in ship.crew:
                                            if isinstance(op, Operator) and op.last_name.lower() == operator_name:
                                                member.act(op)
                                                break
                                        else:
                                            print("Opérateur non trouvé.")
                                    trigger_random_event(fleet)
                                    found = True
                                    break
                            if found:
                                break
                    if not found:
                        print(f"Aucun membre nommé {member_name} n'a été trouvé dans le vaisseau {ship_name}.")
                case _:
                    print("\nChoix invalide.")

        case "0":
            print("\nAu revoir :)")
            break

        case _:
            print("\nChoix invalide, réessayez.")