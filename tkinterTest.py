from tkinter import *
import random

top = Tk()
songList = []
myRolls = []

def printSongList():
    print(songList)

def exportSongList():
    with open("songList.txt", "w") as f:
        for song in songList:
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
        songList.append(E1.get())
        E1.delete(0, END)
        
    clearWindow()

    #This is a Label widget
    L1 = Label(top, text="ourTunes")
    L1.grid(column = 0, row = 1)

    #This is a Text Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    #This is a Button widget
    B1 = Button(text = " + ", bg = "white", command = addSong)
    B1.grid(column = 1, row = 2)

    B2 = Button(text="Print List", bg = "#d4850f", command = printSongList)
    B2.grid(column = 0, row = 1)

    B3 = Button(text="Export List", bg = "#4940e6", command = exportSongList)
    B3.grid(column = 1, row = 3)

    B4 = Button(text="Main Menu", bg = "yellow", command = mainMenu)
    B4.grid(column = 0, row = 3)

def week2():
    def rollDice():
        rollTimes = E2W2.get()
        dieType = E1W2.get()

        clearWindow()
        
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))

        L4W2 = Label(top, text= "Here are your rolls!" )
        L4W2.grid(column= 0, row= 1)
        
        L5W2 = Label(top, text= "{}".format(myRolls))
        L5W2.grid(column= 0, row= 3)

        B2W2 = Button(text= "Main Menu", bg= "yellow", command = mainMenu)
        B2W2.grid(column= 2, row= 4)

    clearWindow()

    L1W2 = Label(top, text= "Dice Roller App")
    L1W2.grid(column=2, row=0)
    
    L2W2 = Label(top, text= "# of Sides")
    L2W2.grid(column=0, row=2)
    
    L3W2 = Label(top, text= "# of Rolls")
    L3W2.grid(column=3, row=2)

    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column=0, row=3)
    
    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column=3, row=3)

    B1W2 = Button(text="Roll 'em", bg = "yellow", command = rollDice)
    B1W2.grid(column=2, row=4)

def week3():
    
    clearWindow()
    
    L1W3 = Label(top, text= "Check back later!")
    L1W3.grid(column=2, row=0)

    B1W3 = Button(top, text= "Main Menu", command= mainMenu)
    B1W3.grid(column=2, row=2)







if __name__ == "__main__":
    mainMenu()
    top.mainloop()
