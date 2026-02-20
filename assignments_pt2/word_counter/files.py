#IC CP2 1st Word counter: files


def file_access():
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("The file was not found")
    except PermissionError:
        print("You do not have permission to access this file")