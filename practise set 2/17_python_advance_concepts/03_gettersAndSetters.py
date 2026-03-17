class Employee:
    def __init__(self, name, salary):
        # constructor runs automatically when object is created
        self.name = name      # full name (example: "jack doe")
        self.salary = salary  # employee salary
    
    @property
    def first_name(self):
        # getter method → called when we access e.first_name
        l = self.name.split(" ")   # split full name into list ["jack","doe"]
        return l[0]                # return first word → first name
    
    @first_name.setter
    def set_first_name(self, first):
        # setter method → called when we assign e.first_name = "john"
        l = self.name.split(" ")      # split current name
        new_name = f"{first} {l[1]}"  # replace first name, keep last name
        self.name = new_name          # update full name


# creating object
e = Employee("jack doe", 550)

# accessing property (calls getter)
print(e.first_name)   # Output → jack

# setting property (calls setter)
e.first_name = "john"

# checking updated full name
print(e.name)         # Output → john doe