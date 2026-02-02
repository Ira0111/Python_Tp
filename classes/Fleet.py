from classes.Member import*
from classes.Operator import*
from classes.Spaceship import*
from classes.Mentalist import*

class Fleet:
    def __init__(self, name):
        self._name = name
        self._spaceships = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def spaceships(self):
        return self._spaceships

    @spaceships.setter
    def spaceships(self, value):
        self._spaceships = value

    def append_spaceship(self, spaceship: Spaceship):
        if len(self.spaceships) >= 15:
            print("La Flotte est complette : imposible d'ajouter", spaceship.name)
        else:
            self.spaceships.append(spaceship)

    def remove_spaceship(self, ship_name):
        for ship in self.spaceships:
            if ship.name.lower() == ship_name.lower():
                self.spaceships.remove(ship)
                print(f"Le vaisseau {ship_name} a été supprimé de la flotte {self.name}")
                return True
        print(f"Aucun vaisseau nommé {ship_name} trouvé dans la flotte {self.name}")
        return False

    def statistics(self):
        total_members = 0
        role_count = {}
        total_experience = 0
        operator_count = 0
        num_merchant = 0
        num_guerre = 0
        num_operational = 0
        num_damaged = 0
        for ship in self.spaceships:
            if ship.shipType.lower() == "marchand":
                num_merchant += 1
            if ship.shipType.lower() == "guerre":
                num_guerre += 1    
            if ship.condition.lower() == "opérationnel":
                num_operational += 1
            else:
                num_damaged += 1
            for member in ship.crew:
                total_members += 1
                role = None
                if isinstance(member, Operator):
                    operator_count += 1
                    total_experience += member.experience
                    role = member.role
                elif isinstance(member, Mentalist):
                    role = "mentaliste"
                else:
                    role = "inconnu"
                role_count[role] = role_count.get(role, 0) + 1
        print("\n\n===Statistiques de la flotte===", self.name)
        print("\nVaisseaux :", len(self.spaceships))
        print("Marchands :", num_merchant)
        print("Guerre :", num_guerre)
        print("Opérationnels :", num_operational)
        print("Endommagés :", num_damaged)
        print("\nNombre total de membres :", total_members)
        print("Répartition des rôles :")
        for role, count in role_count.items():
            print("-", role, ":", count)
        if operator_count > 0:
            moyenne = round(total_experience / operator_count, 2)
            print("Niveau moyen d'expérience des opérateurs :", moyenne)
        else:
            print("Aucun opérateur dans la flotte.")
            
    def update_fleet(self, name=None):
        if name is not None:
            self.name = name
        print(f"La Flotte est renommée en {self.name}.")
