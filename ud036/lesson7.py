# Lesson 7

class Parent(object):
    MALE = "male"
    FEMALE = "female"

    def __init__(self, name=None, gender=None):
        self.name = name
        self.gender = gender

    def __str__(self):
        return "My name is {}. I'm {}.".format(self.name, self.gender)

class Child(Parent):
    def __init__(self, name, gender, annoyance_level=11):
        Parent.__init__(self, name, gender)
        self.annoyance_level = annoyance_level

    def __str__(self):
        return Parent.__str__(self) + " I'm rated {}/10 on the annoyance scale.".format(self.annoyance_level)


bob = Parent("Bob", Parent.MALE)
# print(Parent.__module__)
# print(Parent.__name__)
print(bob)
julie = Child("Julie", Parent.FEMALE)
# print(Child.__module__)
# print(Child.__name__)
print(julie)
