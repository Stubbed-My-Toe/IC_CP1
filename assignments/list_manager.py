# IC 1st Shopping List Manager

print("What items are on your shopping list? To add an item, enter 'add'. To remove an item, enter 'remove'. To print your list, enter 'print'. To finalize and print your total list, enter 'exit'.\n")
shop_list = []
while True:
    action = input("Would you like to 'add', 'remove', 'print', or 'exit'?\n").lower().strip()
    if action == "add":
        new_thing = input("What would you like to add?\n").strip().lower()
        shop_list.append(new_thing)
    elif action == "remove":
        delete = input("What would you like to remove?\n").strip().lower()
        if delete in shop_list:
            shop_list.remove(delete)
        else:
            print("Please try again.")
    elif action == "print":
        show = print(shop_list)
    elif action == "exit":
        print(shop_list)
        break
    else:
        print("You entered an invalid command or item please try again.")