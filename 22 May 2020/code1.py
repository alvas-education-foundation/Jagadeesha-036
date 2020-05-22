username = 'Jaggu''
password = '1111'

userInput = input("Enter your username\n")

if userInput == username:
    a=input("Password?\n")   
    if a == password:
        print("Welcome!")
    else:
        print("Wrong password..!!!")
else:
    print("Incorrect username.")