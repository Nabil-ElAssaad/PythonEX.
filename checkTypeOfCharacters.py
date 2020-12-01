char = input("Please enter a char\t" )
if char.isalnum():
    print(char ," is a num")
    if char.isalpha():
        print(char, " is a Alfa")
        if char.islower():
            print(char , " is lower case")
        else:
            print(char, " is upper case")
    else:
        print(char ," is a  digit")
else:
    print("its space or something else")