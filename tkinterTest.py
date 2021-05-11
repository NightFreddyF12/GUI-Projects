from tkinter import *

top = Tk()
playlist = []

def printList():
    print(playlist)

def exportPlaylist():
    with open("playlist.txt", "w") as f:
        for song in playlist:
            f.write("%s\n" % song)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI's")
    LMain.grid(column = 0, row = 1)

    B1Main = Button(text="Week 1", bg = "White", command = week1)
    B1Main.grid(column = 0, row = 2)

    B2Main = Button(text="Week 2", bg = "White", command = week2)
    B2Main.grid(column = 0, row = 3)

    B3Main = Button(text="Week 3", bg = "White")
    B3Main.grid(column = 0, row = 4)

def week1():
    
    def addSong():
        playlist.append(E1.get())
        E1.delete(0, END)
        
    clearWindow()

    #This is a Label widget
    L1 = Label(top, text="Playlist Generator")
    L1.grid(column = 0, row = 1)

    #This is a Text Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    #this is a Button widget
    B1 = Button(text=" + ", bg = "#B4F9FF", command = addSong)
    B1.grid(column = 1, row = 2)

    B2 = Button(text="Print List", bg = "Orange", command = printList)
    B2.grid(column = 0, row = 3)

    B3 = Button(text="Export List", bg = "#8a7e42", command = exportPlaylist)
    B3.grid(column = 1, row = 3)

    Bclear = Button(text="Main Menu", bg = "Red", command = mainMenu)
    Bclear.grid(column = 1, row = 4)

def week2():
    clearWindow()

    L1W2 = Label(top, text= "Dice Roller App")
    L1W2.grid(column=2, row=1)
    
    L2W2 = Label(top, text= "# of Sides")
    L2W2.grid(column=0, row=2)
    
    L3W2 = Label(top, text= "# of Rolls")
    L3W2.grid(column=3, row=2)

    E1W2 = Label(top, bd = 5)
    E1W2.grid(column=0, row=3)
    
    E2W2 = Label(top, bd = 5)
    E2W2.grid(column=3, row=3)

    B1W2 = Label(text="Roll 'em", bg = "yellow")
    B1W2.grid(column=2, row=4)








if __name__ == "__main__":
    mainMenu()
    top.mainloop()
