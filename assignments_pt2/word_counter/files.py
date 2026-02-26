#IC CP2 1st Word counter: files

from timey_wimey import show_time

def word_count(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return 0
    
def file_access_read(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("The file was not found")
    except PermissionError:
        print("You do not have permission to access this file")

def file_access_write(file_path):
    try:
        with open(file_path, 'a+') as f:
            f.write(input('Line to write: ')+'\n')
            while True:
                if input("Y to write another line?\n").lower()=='y':
                    f.write(input('Line to write: ')+'\n')
                else:
                    break
                f.write(f"{show_time()}")
                f.write(f"{word_count(file_path)}")
    except FileNotFoundError:
        print("The file was not found")
    except PermissionError:
        print("You do not have permission to access this file")

    
