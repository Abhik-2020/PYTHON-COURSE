# 2. create a list [1, 2, 3, 4, 5] and use map() with lamda function to get their squares

number = [1, 2, 3, 4, 5]
square = lambda x: x*x

print(list(map(square, number)))
