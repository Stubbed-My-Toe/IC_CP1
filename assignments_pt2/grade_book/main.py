#IC CP2 Simple Grade Book

#main menu
def main_menu(main_menu_choice):
    print("""=====================================
    SIMPLE GRADE BOOK 
    =====================================

    Welcome to the Class Grade Book!""")

    print("""MAIN MENU:
    [1] Add New Student
    [2] Add Grade to Student
    [3] View Student Record
    [4] View All Students
    [5] Class Summary
    [6] Exit""")

    main_menu_choice = ("Enter your choice (1-6): ")
    if main_menu_choice == "1":
        #add new student
        pass
    elif main_menu_choice == "2":
        #add grade to student
        pass
    elif main_menu_choice == "3":
        #View student record
        pass
    elif main_menu_choice == "4":
        #view all students
        pass
    elif main_menu_choice == "5":
        #class summary
        pass
    elif main_menu_choice == "6":
        #exit
        pass
    else:
        print("Please try entering your choice again")
        main_menu()