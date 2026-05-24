#Denomination Calculator app for money
from tkinter import *
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination Calculator")
root.configure(bg = "lightblue")
root.geometry("650x400")

upload = Image.open("Money denomination.jpg")
upload = upload.resize((300, 300))
upload_image = ImageTk.PhotoImage(upload)

label = Label(root, image=upload_image, bg="lightblue")
label.place(x=180, y=20)

label1 = Label(root, text="Welcome to Denomination Calculator", bg="lightblue")
label1.place(relx=0.5, y=340, anchor=CENTER)

def Home_screen():
    answer = messagebox.askyesno("Alert", "Do you want to calculate the denomination count?")
    if answer:
        topwin()

button1 = Button(root, text="Let's get started!", command=Home_screen, bg="brown", fg="white")
button1.place(x=260, y=360)

def topwin():
    top = Toplevel(root)
    top.title("Denomination Calculator")
    top.geometry("600x350+50+50")

    label = Label(top, text="Enter total amount", bg="lightgrey")
    entry = Entry(top)
    
    lbl = Label(top, text="Here are number of notes for each denomination", bg="lightgrey")

    l1 = Label(top, text="2000", bg="lightgrey")
    l2 = Label(top, text="500", bg="lightgrey")
    l3 = Label(top, text="100", bg="lightgrey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            amount = int(entry.get())

            note2000 = amount // 2000
            amount %= 2000

            note500 = amount // 500
            amount %= 500

            note100 = amount // 100
            amount %= 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(0, str(note2000))
            t2.insert(0, str(note500))
            t3.insert(0, str(note100))

        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
    btn = Button(top, text="Calculate", command=calculator, bg="brown", fg="white")

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)
           
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
            
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    top.mainloop()

root.mainloop()