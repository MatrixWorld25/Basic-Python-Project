#Creating a todo list using python 
#At first create an Empty list
todo = []

# use a function to add in list
def adding_task():
        task=input("Enter a task which you want to add:")
        todo.append(task)
        print(f"Task '{task}' successfully added.")
    
#Use a function to delete a tasks from list
def deleting_task():
        try:
            TaskToDelete=int(input("Please enter a digit to delete:"))
            if TaskToDelete >=0 and TaskToDelete<len(todo):
                todo.pop(TaskToDelete)
            else:
                print(f"Task'{TaskToDelete}'was not found.")    
            
        except:
            print("You enter a invalid input try again")
        
#use a function to show the contents in the list
def showing_task():

    if (len(todo )!=0):
        print("Your present todo list is : ")
        for index in enumerate(todo,start=1):
            print(index,end='')  
    else:
    
        print("Your todo list is empty now.")  
        
#use the main loop to execute
while True:
    print("\n Todo list main menu are:")
    print("1. To Add Task in list:")         
    print("2. To Delete Task from the list:")
    print("3. To Show the current list:")      
    print("4. Exit")
    
    select = int(input("Enter your Task  1/2/3/4 : "))
    
    if select == 1:
        print("Enter your task to add: ")
        adding_task()
        
    elif select == 2:
        print("Your task is successfully deleted. ")    
        deleting_task()
        
    elif select == 3:
        showing_task() 
        print("\nIt is your todo list now.")
        
    elif select == 4:
        print("Goodbye!") 
        break  
      
    else:
        print("You select a invalid Digits. try again")

#code is made by Ayan Roy              