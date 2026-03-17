#write a program using match case that simulates a simple calculator.
  #1. ask the user for number and an operation (+,-,*,/)
  #2. perform the opration using match case.

num1 = int(input("Enter a first  number"))
num2 = int(input("Enter a second number"))

operation = input("choose opration")

match operation :
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 * num2)
