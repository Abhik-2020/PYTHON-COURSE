class Employee:
    def __init__(self, salary, name, bond):
        self.salary = salary # Create an instance attribute of name salary and assign it with salary
        self.name = name 
        self.bond = bond

    def get_salary(self):
        return self.salary
        
    def get_info(self):
        print(f"the name of the Employee is {self.name}. salary is {self.salary}. the bond is for {self.bond} years")

e1 = Employee(34000, "john doe", 4)
# print(e1.self.salary())
e1.get_info()

e2 = Employee(200, "anmol", 1)
e2.get_info()
     