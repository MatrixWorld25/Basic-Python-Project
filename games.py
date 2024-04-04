#creats a rock,paper,scissor game
import random

#initially puts the computer and user score
computer_score= 0
user_score= 0

#use the main loop
while True:
    
    user_selection= input('Enter your choice Rocks/Paper/Scissors:- ')
    possible_input = ['Rocks','Paper','Scissors']
    computer_selection = random.choice(possible_input)
    print(f"Your Choice : {user_selection},\nComputer Choice : {computer_selection}")
    if user_selection == computer_selection:
        print(f"Your choice {user_selection} is same with computer choice \nSo Match is Tie")
        
    elif user_selection == 'Rocks':
        if computer_selection == 'Scissors':
            print("You win the match.\nBecause Rocks brokes the Scissors.")
            user_score=user_score+1
            
        else:
            print("You loss the match.\nBecause the Paper covers the Rocks.  ")     
            computer_score=computer_score+1
            
            
    elif user_selection == 'Scissors':
        if computer_selection == 'Rocks':
            print("You loss the match.\nBecause Rocks brokes the scissors.")
            computer_score=computer_score+1
            
        else:
            print("You win the match.\nBecause Scissors cut the Paper.")
            user_score=user_score+1
            
            
    elif user_selection == 'Paper':
        if computer_selection == 'Rocks':
            print("You win the match.\nBecause Paper covers the Rocks.")
            user_score=user_score+1
            
        else:
            print("You loss the match.\nBecause Paper was cutting by Scissors.")
            computer_score=computer_score+1
    else:
        print("You choice a invalid Strings.")
    
    #use a while loop for user want any more time or not       
    while True:
                
        want_anymore = input("Are you want play again {yes/no/score} : ")
        possible = ['yes','no','score']
        
        if want_anymore in possible:
            break
        else:
            print("Please choose the correct option..\n")
            
    if want_anymore =='no':
            print(f"Thanks to play.\nGoodbye!\nUser score is: {user_score}\nComputer Score is: {computer_score}")
            break
                
    elif want_anymore == 'score':
            print(f'User score is: {user_score}\nComputer score is: {computer_score}')    
                    
    elif want_anymore == 'yes':
            print("Ok.\nLet's play more:")  
    
 #code is made by Ayan Roy                                         