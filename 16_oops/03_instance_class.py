class Employee:
    comapany = "Asus" # This is class attribute 

    def __init__(self, salary, name, bond, comapany):
        self.salary = salary #create an instance attribute of name and assihgn it with salary 
        self.name = name
        self.bond = bond
        self.comapany = comapany

    # def get_salary(self):
    #     return self.salary
    
    def get_info(self):
        print(f"The name of employee is{self.name}, salary is {self.salary}. The bond is for {self.bond}years")

e1 = Employee(300, "Abhik", 2, "tesla")
print(e1.comapany) #will always print instance attribute whenever present 
print(Employee.comapany) # This will always print the class attribute
# print(e1.salary)
e1.get_info() 

# print(e1.get_info()) #it wriren none


# object intropection
print(dir(e1))