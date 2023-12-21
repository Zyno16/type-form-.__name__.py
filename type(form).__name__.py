from tkinter import *
from tkinter import ttk
import tools
form =Tk()
form.geometry("700x500")
Label(form,text ="hello everyone").pack()
Label(form,text ="welcome to cairo").pack()
Button(form,text="ok").pack()
Button(form, text ="show").pack()
Entry(form).pack()
Entry(form).pack()

ttk.Label(form,text ="hello everyone").pack()
ttk.Label(form,text ="welcome to cairo").pack()
ttk.Button(form,text="ok").pack()
ttk.Button(form, text ="show").pack()
ttk.Entry(form).pack()
ttk.Entry(form).pack()
frame =Frame(form)
ctr =form.winfo_children()
for c in ctr:
    #print(type(c))
    print("..........")
    print (type(c).__name__ )
    
   



