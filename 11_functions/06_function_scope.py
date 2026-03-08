def sum(a, b):
    #a and b are local variables 
    c = a + b
    z = 1 #it creats a local variables called z which is destroyed after this function return 
    return c

def greet():
    z = 32 # local variable
    print("hello")

z = 8 # z is a global variable
print(z)
print(sum(4, 4))
print(z)