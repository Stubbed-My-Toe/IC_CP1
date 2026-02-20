#IC CP2 1st word counter

from files import file_access

def wrdcount_main(main_choice):
    print("--- Document Word Count Updater ---\n1. Update document info\n2. View document\n3. Add content to document\n4. Exit")
    main_choice = input("Enter your choice (1-4): ")
    if main_choice == "1":
        #update document info
        file_path = ("\nEnter the exact file path for your document: ")
        pass
    elif main_choice == "2":
        #print(document)
        pass
    elif main_choice == "3":
        #add content to document
        pass
    elif main_choice == "4":
        #exit()
        pass
    else:
        print("\nInput invalid. Please try again.")
        wrdcount_main()