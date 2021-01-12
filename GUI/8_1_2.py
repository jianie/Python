from tkinter import *

def changeColor(event):          
    if entName["fg"] == "blue": 
        entName["fg"] = "red"
    else:
        entName["fg"] = "blue"
        
window = Tk()     
window.title("Entry widget")
entName = Entry(window, fg="blue")
entName.grid(padx=100, pady=15)
entName.bind("<Button-3>", changeColor)
window.mainloop()




