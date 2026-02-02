from classes.Member import*

class Operator(Member):
    def __init__(self, first_name, last_name, gender, age, role, experience = 0):
        super().__init__(first_name, last_name, gender, age)
        self._role = role.lower()
        self._experience = experience

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value

    def act(self):
        match self.role:
            case "commandant":
                print(self.first_name, self.last_name, "fait des verification")
            case "technicien":
                print(self.first_name, self.last_name, "nettoie le vaisseau")
            case "armurier":
                print(self.first_name, self.last_name, "fabrique une arme")
            case "pilote" | "pilot":
                print(self.first_name, self.last_name, "s'entrainne sur un simulateur")
            case "marchand":
                print(self.first_name, self.last_name, "surveil son stock")
            case "entretien":
                print(self.first_name, self.last_name, "effectue la maintenance du vaisseau")
            case _:
                print(self.first_name, self.last_name, "rôle inconnu")   

    def gain_experience(self):
        self.experience += 1

    def update_operator(self, first_name=None, last_name=None, gender=None, age=None, role=None, experience=None):
        self.update_member(first_name, last_name, gender, age)
        if role is not None:
            self.role = role
        if experience is not None:
            self.experience = experience
        print(f"L'Opérateur {self.first_name} {self.last_name} est mis à jour.")
