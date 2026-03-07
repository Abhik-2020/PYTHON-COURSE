s = "hello world" #String are immutable


#s[0] = "R" #you cannot do this 

a = len(s)
print(a)

#print(s.upper(),s)
# print(s.upper()) 
# print(s.lower())
# print(s.capitalize())
# print(s.title())


# strip :- removes the extra spaces or unwanted characters from the begining and end of a string
# text = " \n Hello world "
# print(text.strip())  #output : "hello world"
# print(text.lstrip()) #output : "hello world "
# print(text.rstrip()) #output :" hello world"

# text = "Python is fun, fun and fun"
# print(text.find("is")) #output 7 index of first occurence
# print(text.replace("fun", "awesome"))

# text = "apples,banana,pineapples"
# print(text.split(","))

# print(",".join(['apples', 'banana', 'pineapples']))

# text = "Python123"
# print(text.isalpha())
# print(text.isdigit())
# print(text.isalnum())
# print(text.isspace())