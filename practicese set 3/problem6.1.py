# Q6. bonus question 
# 1. write a program that counts how many vowels are a given string.
# 2. take user input string and check if it is a palondrome(same forward and backward)

sentence = "coding in python is fun"
sum = 0
vowels = ["a", "e", "i", "o", "u"]

for char in sentence.lower():
    if(char in vowels):
        sum += 1

print(f"There are {sum} vowels in this sentance")