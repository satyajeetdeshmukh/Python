from tkinter import *

root = Tk()

one = Label(root, text='One',  bg="red", fg="white")
one.pack()

two = Label(root, text="two", bg="blue", fg="white")
two.pack(fill=X)


three = Label(root, text="three", bg="yellow", fg="black")
three.pack(side=LEFT, fill=Y)

root.mainloop()