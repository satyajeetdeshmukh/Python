from tkinter import *

def CreateFiles(event):
    for num in range(1,eval(entry_1.get())+1):
        with open(str(num)+'.py','w') as f:
            pass
    exit()

if __name__ == '__main__':
    root = Tk()

    label_1 = Label(root, text='Enter no. of files to be gerated and press Enter!')
    entry_1 = Entry(root)

    label_1.grid(row=0) # E for east
    entry_1.grid(row=1)

    entry_1.bind("<Return>", CreateFiles)

    root.mainloop()

