# class :  class is blueprint or a template. eg. form for an exam that contain name, age, elective, father's name etc.

#object : specific instance created from the template(class). eg. from which contains the data for jonh doe

class Employee:
    company = "HP"
    
    def get_salary(self): #self is important here because self is a way to refrence the object of the class which is being created 
        return 34000
    

e1 = Employee() # An object of class Employee is created here
print(e1.get_salary()) # Employee e's get salary method is called 

e2 = Employee()
print(e2.get_salary())
print(e1.company)
