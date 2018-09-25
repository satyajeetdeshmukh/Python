# gui with classes
from tkinter import *

class BuckyButtons:

    def __init__(self, master): # when object is created this function will initialize, master means the main window
        frame = Frame(master)
        frame.pack()


        self.printButton = Button(frame, text="Chello", command = self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Ula lala lelo Ula lala lelo")




root = Tk()
b = BuckyButtons(root)
root.mainloop()
