#create a contact list using python and add,search,show,delete,update the contact list
contact_list = {}

#creat a fuction to add name , number
def add_contacts():
    Name = input("Name:-")
    phone = input("Phone Number:-")
    contact_list[Name]=phone
  

#creat a function to search     
def search_contacts():
    search = input("Searching Name:-")    
    if search in contact_list:
        print(f"{search} contact number is ",contact_list[search])
        
    else:
        print(f"Cannot find {search} in contact list")    

#creat function to show contacts        
def show_contacts():
    print("Name\t\t\t\tPhone number")
    for key in contact_list:
        print("{}\t\t\t\t{}".format(key,contact_list.get(key)))

#creat a function for updating        
def update_contacts():
    update_contacts = input("Contacts to be update:")  
    
    if update_contacts in contact_list:
        phone = input("Enter Mobile number:")
        contact_list[update_contacts]=phone 
        
    else:
        print("Your choice is not in contact list.")      

#creat a function for deleting        
def delete_contacts():
    try:
        NumberToDelete = input("Enter the deleting name:")
        if NumberToDelete in contact_list:
            contact_list.pop(NumberToDelete)
        else:
            print(f"{NumberToDelete} is not found in contact list")
    except:
        print("You enter a invalid number.")

# using the main loop        
while True:
                     
 print("--: Welcome to our contact list :-- ")    
 print("-----------------------------------")     
 print("1.Add the number:-")
 print("2.Search the contacts:-")
 print("3.Show the contacts:-")
 print("4.Update the contacts:-")
 print("5.Delete the contacts:-")
 print("6.To exit")
 
 #user select the options
 select = input("Please select what you want {1/2/3/4/5/6} :-")  
 possible = ['1','2','3','4','5','6']

 if select == '1':
     add_contacts()
     
 elif select == '2':
     search_contacts()
 
 elif select == '3':
     show_contacts()
     
 elif select == '4':
     update_contacts()
     
 elif select == '5':
     delete_contacts()
 elif select not in possible:
     print("Please select correct option")
 elif select == '6':
     print("Goodbye!")  
     break          
 
 #code is made by Ayan Roy