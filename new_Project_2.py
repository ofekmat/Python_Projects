import json
import os
import pandas as pd
def printMenu():                         
    print("1. Save a new entry ")
    print("2. search by ID ")
    print("3. Print ages average ")
    print("4. Print all names ")
    print("5. Print all IDs ")
    print("6. Print all entries ") 
    print("7. Print users by index ")
    print("8. save all data ")
    print("9 exit ")
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
        
def saveAllData(users_dict):
    path = "/Users/ofek_matlov/Desktop/python_new/"
    output = []
    json_path = path + "ofek.json"
    if not os.path.exists(json_path):
        print("Error: path is not exist :" + json_path)
        return
    with open(json_path) as json_file:
        header_line = json.load(json_file)
        if len(header_line) < 3:
            print("Error: must be have 3 line ")
            return
    for i in users_dict:
        new_user = {}
        new_user[header_line[0]] = i
        new_user[header_line[1]] = users_dict[i]["Name"]     
        new_user[header_line[2]] = users_dict[i]["Age"]
        output.append(new_user)

    output_file_name = input("Please enter output file name: ")
    user_dict_df = pd.DataFrame(output)
    user_dict_df.to_csv(path + output_file_name, index = False)

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
            saveAllData(users_dict)    
        elif user_choice == "9":
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



    



