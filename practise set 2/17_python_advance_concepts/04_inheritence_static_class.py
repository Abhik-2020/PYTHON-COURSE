class Employee: 
    company = "hp"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    # inctance method (default)
    def print_info(self):
        info = f"the name is: {self.name} and the salary is: {self.salary}"
        print(info)

    # static method    
    @staticmethod
    def sum(a,b):
        return a+b
    
    #class method
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


    
e1 = Employee("jack", 3500)
e2 = Employee("jill", 3400)
# print(Employee.company)
# print(Employee.name) #this will throw an error

e1.print_info()
e2.print_info()

# print(sum(4,5)) #it will throw an error
print(e1.sum(4,5))

print(e1.company)
print_company("asur")
print(e1.coampany)

print(Employee.company)
e1.change_company("acer")
print(Employee.company)

