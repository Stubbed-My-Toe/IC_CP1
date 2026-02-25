#IC CP2 1st Word counter: files

from timey_wimey import show_time

def file_access_read():
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("The file was not found")
    except PermissionError:
        print("You do not have permission to access this file")

def file_access_write():
    try:
        with open(file_path, 'a+') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("The file was not found")
    except PermissionError:
        print("You do not have permission to access this file")

    
