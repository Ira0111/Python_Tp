from classes.Member import*
from classes.Operator import*

class Mentalist(Member):
    def __init__(self, first_name, last_name, gender, age, mana = 100):
        super().__init__(first_name, last_name, gender, age)
        self._mana = mana 

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        self._mana = max(0, min(100, value))

    def act(self, operator):
        if self.mana <20:
            print(self.first_name, self.last_name, "n'as pas assez de mana pour influencer", operator.first_name, operator.last_name)
        else:
            self.mana -= 20
            print(self.first_name, self.last_name, "influence", operator.first_name, operator.last_name, "pour agir :")
            operator.act()
        
    def recharge_mana(self):
        self.mana = min(100, self._mana + 50)
        print(self.first_name, self.last_name, "recharge son mana à", self.mana)

    def update_mentalist(self, first_name=None, last_name=None, gender=None, age=None, mana=None):
        self.update_member(first_name, last_name, gender, age)
        if mana is not None:
            self.mana = mana
        print(f"Le mentaliste {self.first_name} {self.last_name} est mis à jour.")

