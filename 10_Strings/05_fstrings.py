#string formating 

template = "Dear {}, you are awsome. take this {}$ bag"
a = "john"
a1 = 10000
b = "jack"
b1 = 20000
c = "marie"
c1 = 300

s1 = template.format(a,a1)
print(s1)


#f-strings

print(f"{a} you are awsome and take this {a1}$ bag")
