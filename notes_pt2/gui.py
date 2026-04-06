#IC CP2 Tkinter GUI Notes
import tkinter as tk

count = 1

root = tk.Tk()

root.title("Testing")
root.configure(background = "green")
root.minsize(250, 250)
root.geometry("300x300+100+100")
label = tk.Label(root, text = """This is currently working!""", font = ("Times New Roman", 14))
label.config(fg="blue", background = "green")
label.pack()

def add():
    global count
    root.count += 1
    tk.Label(root, text = root.count).pack
    
show_count = tk.Label(root, text = count)
show_count.pack()
button = tk.Button(root, text = "ADD YOU BUM!", command = add)
button.pack
root.count = 0

#image = tk.PhotoImage(file = "images/the_maxx.png")
#tk.Label(root, image=image).pack()

root.mainloop()