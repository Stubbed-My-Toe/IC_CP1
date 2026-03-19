#IC CP2 Geometry Simulator

#BIG WELCOME
print("Welcome to the Geometry Calcutor!")

#main menu for choosing actions
def main_menu(picked_action):
    print("""=====================================
    GEOMETRY CALCULATOR
    =====================================

    Welcome to the Shape Calculator!

    =====================================
    MAIN MENU 
    =====================================""")

    #options for actions to perform
    def actions():
        picked_action = input("""ACTIONS:
        [1] Create New Shape
        [2] View All Shapes
        [3] Select Shape
        [4] Compare Shapes
        [5] Sort Shapes
        [6] Formula Guide
        [7] Quit

        Enter your choice (1-7): """).strip()
        return picked_action
    
    actions()

    if picked_action == "1":
        pass
    elif picked_action == "2":
        pass
    elif picked_action == "3":
        pass
    elif picked_action == "4":
        pass
    elif picked_action == "5":
        pass
    elif picked_action == "6":
        pass
    elif picked_action == "7":
        exit()
    else:
        print("Please try again")
        actions()