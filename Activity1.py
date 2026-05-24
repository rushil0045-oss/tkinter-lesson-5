from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Top window")

def topwin():
    top = Toplevel()
    top.geometry("200x150")
    top.title("Top window")
    label = Label(top, text="This is the top window")
    label.pack()
    top.mainloop()

label = Label(root, text="This is the main window")
btn = Button(root, text="Open the top window", command=topwin)
label.pack()
btn.pack()

root.mainloop()