#create a calculator using python programming language
def sum(a,b):
    return a+b

# using function for subtract
def sub(a,b):
    return a-b

#using function for Multiplication
def multiply(a,b):
    return a*b

#using function to divided
def div(a,b):
    return a/b

print("Please select operation: ")
print("1.Addition ")
print("2.Substraction ")
print("3.Multiplication" )
print("4.Division ")

while True:
    #input from user
    select = int(input("Select your choice 1/2/3/4:"))

 # check choice are in 1  2   3  4
    if select in (1 ,2 ,3 ,4 ):
        try:
            x=float(input("Enter the first number:"))
            y=float(input("Enter the second number: "))
        except ValueError:
            print("You enter a invalid input TRY AGAIN")
            continue
    
    if select == 1:
        print(x,"+",y,"=",sum(x,y))

    elif select == 2:
        print(x,"-",y,"-",sub(x,y))
    
    elif select == 3:
        print(x,"*",y,"=",multiply(x,y))
        
    elif select == 4:
        print(x,"/",y,"=",div(x,y))
        
    #use break to exit while loop
    want_another = input("Please enter {yes/no}:")
    if want_another == 'no':
        print("Goodbye!")
        break
    else:
        print("OK! \nLet's Enter a valid input:-")                    

#code is made by Ayan Roy