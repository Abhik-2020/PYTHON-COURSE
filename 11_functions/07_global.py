def sum(a, b):
    print("Hey I am summing")
    c = a + b
    global z #please modify global z
    z = 0 # this will refer to global z not local variable
    return c

z = 3
print(sum(4, 4))
print(z)