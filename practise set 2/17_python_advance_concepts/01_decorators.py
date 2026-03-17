# What is a Decorator in Python?

# A decorator is a function that modifies or extends another function’s behavior without changing its actual code.

# 👉 Think of it like a wrapper that adds extra features before or after a function runs.

# decorator is function that takes a function, it creates a new function inside its body (wrapper). then it return that new function
def decorator(func):
    def wrapper():
        print("I am about to execute a function.......")
        func()
        print("I have executed this function....")
    return wrapper

# function without decorators
def say_hello():
    print("hello!")

# What actually decorators works
# say_hello()
# f = decorator(say_hello)
# f()

'''
def f():
        print("I am about to execute a function.......")
        print("hello!")
        print("I have executed this function....")
    
'''

# how decorators called in function (@decorators)
@decorator
def say_hello():
    print("hello!")

say_hello()


# example no.2


# def say_hello():
#     print("Hello!")

# def decorator(func):
#     def wrapper():
#         print("Before function runs")
#         func()
#         print("After function runs")
#     return wrapper

# say_hello = decorator(say_hello)
# say_hello()

