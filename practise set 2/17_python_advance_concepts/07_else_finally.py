try:
    a = 345/10   # This runs without any error

except Exception as e:   
    print(e)   # Runs only if an error occurs

else:
    # Runs only if NO exception occurred in try block
    print("hey i am good")