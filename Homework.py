from tkinter import *
window = Tk()
window.title("Password strength checker App")
window.geometry("400x100")

label = Label(window, text="Enter your password:")
label.pack()
entry = Entry(window, width=30)
entry.pack()
result = Label(window, text="")
result.pack()

def check_password():
    password = entry.get()
    lenght = len(password)

    if lenght > 12:
        result.config(text="Your password is very strong", fg="darkgreen")
    
    elif lenght > 8:
        result.config(text="Your password is strong", fg="Lightgreen")
    
    elif lenght >= 6 and lenght <= 8:
        result.config(text="Your password is medium", fg="yellow")
    
    elif lenght <= 5:
        result.config(text="Your password is weak", fg="red")
    
    
    
   
    
    
button = Button(window, text="Check Password Strength", command=check_password)
button.pack()

window.mainloop()