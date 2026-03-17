# Getters and Setters in Python are methods used to access (get) and modify (set) private variables safely.

# Basic Conc

class Student:
    def __init__(self, name):
        self._name = name   # private variable

    @property
    def name(self):        # getter
        return self._name

    @name.setter
    def name(self, value): # setter
        if len(value) < 3:
            print("Name too short")
        else:
            self._name = value


s = Student("Abhik")
print(s.name)   # getter called

s.name = "Al"   # setter called
s.name = "Rahul"
print(s.name)