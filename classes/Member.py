class Member:
    def __init__(self, first_name, last_name, gender, age):
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender.lower()
        self._age = age

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    def introduce_yourself(self):
        if self.gender == "femme":
            print("Je suis", self.first_name, self.last_name, "je suis une femme de", self.age, "ans.")
        elif self.gender == "homme":
            print("Je suis", self.first_name, self.last_name, "je suis un homme de", self.age, "ans.")

    def update_member(self, first_name=None, last_name=None, gender=None, age=None):
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if gender is not None:
            self.gender = gender
        if age is not None:
            self.age = age
        print(f"Le membre {self.first_name} {self.last_name} est mis à jour.")
