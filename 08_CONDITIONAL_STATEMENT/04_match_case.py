a = (int(input("Enter a lucky number between 1 to 10")))

match a:
    case 6:
        print("you won charger")
    case 4: 
        print("you won mobile phone")
    case 3:
        print("you won 3 dollar")
    case _:
        print("better luck nrxt time")