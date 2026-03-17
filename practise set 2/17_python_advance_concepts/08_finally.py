
def divide(a,b):
    try : 
        c=a/b
        print(c)
        return c

    except Exception as e:   # Print error if division fails (like divide by zero)
        print(e)
        return None

    #  This is always executed no matter if try complrtely executed or not
    finally:
        print("This is always executed")

#  Taking first number input and converting to integer
a = int(input("Enter number 1: "))

# Taking second number input and converting to integer
b = int(input("Enter number 2: "))
divide(a ,b)