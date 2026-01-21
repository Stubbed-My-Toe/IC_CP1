#IC 1st Personal Library

library = []


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
    selected_action = int(input("Select which action you want to perform. Type 1 to view the library, 2 to add a new item, 3 to search the library, 4 to remove an item, and 5 to exit the program.\n"))
    if selected_action == 1:
        view()
    elif selected_action == 2:
        add_item()
    elif selected_action == 3:
        search()
    elif selected_action == 4:
        remove_item()
    elif selected_action == 5:
        print("Exiting Program!")
        exit()
    else:
        print("Please try again.")
        menu()


    

print("Welcome to the Personal Library! This is where you can store books.")

while True:
    menu()
