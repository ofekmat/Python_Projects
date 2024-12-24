def printMenu():                         
    print("1. Save a new Entry ")
    print("2. search by ID ")
    print("3. Print ages average ")
    print("4. Print all names ")
    print("5. Print all IDs ")
    print("6. Print all entries ") 
    print("7. Print users by index ")
    print("8. exit ")
    user_choice = input ("Please enter your choice: ")
    return user_choice

def digitisok(param):
    if param.isdigit():
        return True
    else:
        print("Error: " + param + " is not a number ")
        return  False

def saveNewEntry(users_dict, users_list, sum):
    id = input("ID: ")
    if digitisok(id) == False:
        return -1
    name = input("Name: ")
    age = input("Age: ")
    if digitisok(age) == False:
        return -1    
    if id in users_dict:
        print("Error: ID " + id + "is alredy use. try again")
        return -1
    users_dict[id] = {"Name": name, "Age" : age}
    users_list.append(id)
    print("ID [" + id + "] saved successfuly ")
    sum += int(age)
    return sum  
    
    
def searchById(users_dict):
    id_choice = input("Please Enter your ID you look for: ")
    if id_choice in users_dict:
        printElegant(users_dict,id_choice)
    else:
        print("Error: Id is wrong")
        return    
            
def printAgesAvarage(users_dict, avarage):
    if len(users_dict) != 0:
        print(avarage / len(users_dict))
    else:
        print("Error: Cant divide by zero")
        return       

def printAllNames(users_dict):
    for index, id  in  enumerate(users_dict):
        print(str(index) + " . Name: " + users_dict[id]["Name"])

def printElegant(users_dict, id):
    if id in users_dict:
        print("ID: " + id)
        print("Name: " + users_dict[id]["Name"])
        print("Age: "  + users_dict[id]["Age"])

def printAllIds(users_dict): 
    for index, id in enumerate(users_dict):
        print(str(index) + " Id: " +  id )

def printAllEntries(users_dict):
     for index, id in enumerate(users_dict):
         print(str(index) + ". ")
         printElegant(users_dict, id)

def printUsersByIndex(users_list,users_dict):
    choose_index = int(input("Please Choose index: "))
    if choose_index > len(users_list):
        print("Error: index out of range ")  
        return -1
    else:
       id = users_list[choose_index]
       printElegant(users_dict, id) 
        




def main():
    sum = 0
    users_dict = {}
    users_list = []
    while True:
        user_choice = printMenu()
        if user_choice == "1":
            temp = saveNewEntry(users_dict,users_list, sum)
            if temp != -1:
                sum = temp  
        elif user_choice == "2":
            searchById(users_dict)  
        elif user_choice == "3":
            printAgesAvarage(users_dict, sum) 
        elif user_choice == "4":
            printAllNames(users_dict)
        elif user_choice == "5":
            printAllIds(users_dict)
        elif user_choice == "6":
            printAllEntries(users_dict)                 
        elif user_choice == "7":
            printUsersByIndex(users_list, users_dict)
        elif user_choice == "8":
            exit_input = input("Are you sure? (y/n)")
            if exit_input == "n":
                continue 
            else:
                print("Goodbye")
                break
        else:
            print("Eror: choose number between 1-8 and not something else...")
        continue_input = input("Press Enter to continue: ")        

main()             



    



