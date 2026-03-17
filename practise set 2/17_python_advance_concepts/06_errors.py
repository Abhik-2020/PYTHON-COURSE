# Infinite loop version (currently commented out)
# while True:
#     try:
#         # Taking first number input and converting to integer
#         a = int(input("Enter number 1: "))
#
#         # Taking second number input and converting to integer
#         b = int(input("Enter number 2: "))
#
#         # Performing division and printing result
#         print(f"the division is {a/b}")
#
#     # Handles error if user enters text instead of number
#     except ValueError:
#         print("please dont perform bad typecasts")
#
#     # Handles division by zero error
#     except ZeroDivisionError:
#         print("hey dont divide by 0")
#
#     # Handles any other unexpected error
#     except Exception as e:
#         print("unknown error occurred!", e)


# Taking first number input and converting to integer
a = int(input("Enter number 1: "))

# Taking second number input and converting to integer
b = int(input("Enter number 2: "))

# Checking if denominator is zero
if b == 0:
    # Manually raising an error if user tries to divide by zero
    raise ValueError("please dont divide by 0")

# Performing division and printing result
print(f"The division is {a/b}")