from tkinter import *

top = Tk()
playlist = []

def addSong():
    playlist.append(E1.get())

def printList():
    print(playlist)

#This is a Label widget
L1 = Label(top, text="Playlist Generator")
L1.grid(column= 0, row= 1)

#This is a Text Entry widget
E1 = Entry(top, bd = 5)
E1.grid(column= 0, row= 2)

#This is a Button widget
B1 = Button(text = "Add to playlist!", bg = "light blue", command = addSong)
B1.grid(column = 1, row = 2)

B2 = Button(text = "Export list", bg = "white", command = printList)
B2.grid(column = 1, row = 1)



top.mainloop
