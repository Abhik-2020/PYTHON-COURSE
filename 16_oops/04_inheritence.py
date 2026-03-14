class Animal: #Parent class (super class)
    location = "australia"
    def __init__(self, name):
        self.name = name 

    def speak(self):
        print("Speaking now.....")

    
class Dog(Animal): # This is how inheritence is done in python 
    def speak(self):
        super().speak() # We are using  the speak function of the parent class 
        print("Woof")

# a = Animal("dog")
# a.speak()

d = Dog("bruno")

d.speak()

print(d.name)

print(d.location)