from tkinter import *

root = Tk()

photo = PhotoImage(file='pic.png')
label = Label(root, image=photo)
label.pack()

root.mainloop()
