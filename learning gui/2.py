from tkinter import *

root = Tk() # constructor
# root is a blank window

topFrame = Frame(root)
topFrame.pack() #we have placed 1 invisible container

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Press me HAARRDD", fg="red")
button2 = Button(topFrame, text="Press me HARRDD", fg="yellow")
button3 = Button(topFrame, text="Press me HARDD", fg="green")
button4 = Button(bottomFrame, text="Press me HARD", fg="blue")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)


root.mainloop()