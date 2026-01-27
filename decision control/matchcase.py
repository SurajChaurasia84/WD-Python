x= int(input("Enter a number: "))
match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case _:
        print("Default")
print()