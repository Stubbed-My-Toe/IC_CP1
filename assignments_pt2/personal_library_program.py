#IC 1st Personal Library

import csv
from assignments_pt2 import movies_list
library = [movies_list.csv]


#Prints library
def view():
    print(library)
    menu()


#Adds new items to the list
def add_item():
    new_item = input("What is the item you want to put in?\n").strip()
    library.append(new_item)
    print("Item has been added")
    menu()


#Searches for items using "if item in library"
def search():
    search_item = input("What is the item you want to search for?\n")
    if search_item in library:
        print("Item is in the library!")
        menu()
    else:
        print("Item is not in library.")
        menu()


#Removes items
def remove_item():
    item_tbr = input("What item do you want to remove?\n")
    if item_tbr in library:
        library.remove(item_tbr)
        print("Item deleted!")
        menu()
    else:
        print("Item not found.")
        menu()


#menu: shows what everything is and all the options
def menu():
    selected_action = int(input("Type the number of the item you want to remove. \n1. View a simple list\n2. View a detailed list\n3. Add an item\n4. Update an item\n5. Delete item\n6. Save Library\n7. Reload library from file\n8. Exit (Unsaved data will be lost)\n"))
    if selected_action == 1:
        view()
    elif selected_action == 2:
        view_detailed()
    elif selected_action == 3:
        add_item()
    elif selected_action == 4:
        update_item()
    elif selected_action == 5:
        remove_item()
    elif selected_action == 6:
        save_library()
    elif selected_action == 7:
        rff()
    elif selected_action == 8:
        saveyn= input("Unsaved data will be lost if you exit!\n Do you want to save? Y/N")
        if saveyn == "Y":
            save_library()
            exit()
        elif saveyn == "N":
            exit()
        else:
            print(saveyn)
    else:
        print("Please try again.")
        menu()


    

print("Welcome to the Personal Movie Library! This is where you can store movies.")

while True:
    menu()
