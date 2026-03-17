def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(6)
def say_hello(a):
    print(f"hello {a}")

'''
it replace the fuction say_hello with this:
def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator
'''

say_hello("harry")
