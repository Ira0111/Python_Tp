from classes.Member import*
from classes.Operator import*
from classes.Mentalist import*

class Spaceship:
    def __init__(self, name, shipType, condition="opérationnel"):
        self._name = name
        self._shipType = shipType.lower()
        self._crew = []
        self._condition = condition

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def shipType(self):
        return self._shipType

    @shipType.setter
    def shipType(self, value):
        self._shipType = value

    @property
    def crew(self):
        return self._crew

    @crew.setter
    def crew(self, value):
        self._crew = value


    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        self._condition = value

    def append_member(self, member: Member):
        if len(self.crew) >= 10:
            print("L'équipage est complet : imposible d'ajouter", member.first_name, member.last_name)
        else:
            self.crew.append(member)

    def check_preparation(self):
        has_pilot = False
        has_technician = False
        has_powerful_mentalist = False

        for member in self.crew:
            role = getattr(member, "role", None)
            if role and role.lower() == "pilot":
                has_pilot = True
            elif role and role.lower() == "technicien":
                has_technician = True
            if isinstance(member, Mentalist) and getattr(member, "mana", 0) >= 50:
                has_powerful_mentalist = True

        print("\n🔍 Vérification de la préparation du vaisseau", self.name)
        print("Pilote :", "Check" if has_pilot else "X")
        print("Technicien :", "Check " if has_technician else "X")
        print("Mentaliste avec mana ≥ 50 :", "Check" if has_powerful_mentalist else "X")

        return has_pilot and has_technician and has_powerful_mentalist
    
    def remove_member(self, last_name : str,):
        found = False
        for member in self.crew:
            if member.last_name.lower() == last_name.lower():
                self.crew.remove(member)
                print(member.first_name, member.last_name, "a été retiré de l'équipage du vaisseau", self.name)
                found = True
                return
        if not found:
            print("Aucun membre avec le nom", last_name, "n'a été trouvé dans l'équipage du vaisseau", self.name)

    def display_crew(self):
        print("\n=== Équipage du vaisseau", self.name, "===")
        for member in self.crew:
            role = getattr(member, "role", "inconnu")
            genre_txt = "une femme" if member.gender == "femme" else "un homme"
            if isinstance(member, Operator):
                print(f"- {member.first_name} {member.last_name} est {genre_txt} de {member.age} ans, son rôle est : {member.role}")
            elif isinstance(member, Mentalist):
                print(f"- {member.first_name} {member.last_name} est {genre_txt} de {member.age} ans, c'est un Mentaliste avec {member.mana} mana")

    def update_spaceship(self, name=None, shipType=None, condition=None):
        if name is not None:
            self.name = name
        if shipType is not None:
            self.shipType = shipType
        if condition is not None:
            self.condition = condition
        print(f"Le vaisseau {self.name} est mis à jour.")
