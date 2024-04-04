# creat a password generator using python
#importing a random file
import random
import secrets
import string

while True:
#giving the lenth of password from input
    lenth = int(input("Enter the lenth of password:"))

    character = string.ascii_letters
    character += string.digits
    character += string.punctuation

    password = ""

    for i in range (lenth):
        password += random.choice(character)

    print("Your password will be: ",password)
    
    want_more = input("Are you want more {yes/no}:- ")
    if want_more == 'no' :
        print("Goodbye!")
        break # stop the loop
    
    else:
        print("Ok! \n Let's put the lenth ")
        
        
#code is made by Ayan Roy