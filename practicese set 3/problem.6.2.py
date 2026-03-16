# 2. take user input string and check if it is a palindrome(same forward and backward)


string = input("give a word ")
print(string) #palindrome word :- like madam, level etc.

if(string == string[::-1]):
    print("This word is palindrome")

else:
    print("This word is not palindrome")

    