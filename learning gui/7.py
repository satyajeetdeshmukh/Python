from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo(title='CONGRATULATIONS!!!!!', message='YOU ARE THE FIRST VISITOR, CONGRATS ON WINNNING 1 MIL DOLLARS')

answer = tkinter.messagebox.askquestion('Question 1', 'Do you like cats??')

if answer == 'yes':
    print ('Here is a cat pic')





root.mainloop()