class point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def sum(self, p):
        return point((self.x + p.x), (self.y + p.y))
    
    def print_point(self):
        print(f"X is {self.x}, and t is {self.y}")

    def __add__(self, p):
        return point((self.x + p.x), (self.y + p.y))
    
p1 = point(3, 2)
p2 = point(6, 3)

# p = p1.sum(p2) # return a new point which is sum of p1 and p2 
p = p1 + p2 # we overload the + operator by writing _and_ function 
p.print_point()