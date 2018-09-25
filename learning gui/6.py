# dropdown menu
from tkinter import *

def doNothing() :
    print("Meow.")

def Bark():
    print("Bow Bow")

root = Tk()

#  Main Menu
menu1 = Menu(root)
root.config(menu=menu1)

# Cat Menu
subMenu1 = Menu(menu1)
menu1.add_cascade(label='Cat', menu=subMenu1)
subMenu1.add_command(label='Meow for me!', command=doNothing)
subMenu1.add_command(label='Scratch', command=doNothing)
subMenu1.add_separator()
subMenu1.add_command(label='Exit', command=exit)

# Dog Menu
subMenu2 = Menu(menu1)
menu1.add_cascade(label='Dog', menu=subMenu2)
subMenu2.add_command(label='Bark for me!', command=Bark)
subMenu2.add_command(label='Roll', command=Bark)
subMenu2.add_separator()
subMenu2.add_command(label='Exit', command=exit)

# Toolbar

toolbar = Frame(root, bg="gray")

insertcat = Button(toolbar, text='Insert Cat pics', command=doNothing)
insertcat.pack(side=LEFT, padx=2, pady=2)

insertdog = Button(toolbar, text='Insert Dog pics', command=Bark)
insertdog.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# Status Bar

status = Label(root, text='I show nothing useful', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()