class Person:
    def __init__(self, name):
        self._name = name  # Private attribute

    @property               # getter
    def name(self):
        return self._name

    @name.setter            # setter
    def name(self, new_name):
        self._name = new_name

person = Person("Saifullah")

current_name = person.name
print("Current name:", current_name) 

person.name = "Balghari"
new_name = person.name
print("New name:", new_name)