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

    """
    Program Goals:
    1. Get input from the user (at multiple points) 
    2. We need to convert some of this input to INTs from STRs
    3. We need to provide choices to the user
        a. Add more values to a list
        b. Return a value at a specific index

    """

    import random
    myList = []
    unique_list = []

    def mainProgram():
        while True:
            try:
                print("Hello, there! Let's work with lists!")
                print("Choose from the following options. Type a number below!")
                choice = input("""1. Add to a list
    2. Add a bunch of numbers
    3. Get an item at an index
    4. Sort list
    5. Random search
    6. Linear search
    7. Recursive binary search
    8. Iterative binary search
    9. Print list
    10. Limit the list
    11. Quit   """)
                if choice == "1":
                    addToList()
                elif choice == "2":
                    addABunch()
                elif choice == "3":
                    indexValues()
                elif choice == "4":
                    sortList(myList)
                elif choice == "5":
                    randomSearch()
                elif choice == "6":
                    linearSearch()
                elif choice == "7":
                    binSearch = input("What number are you looking for?   ")
                    recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
                elif choice == "8":
                    binSearch = input("What number are you looking for?   ")
                    result = iterativeBinarySearch(unique_list, int(binSearch))
                    if result != -1:
                        print("Your number is at index position {}".format(result))
                    else:
                        print("Your number is not found in that list, bud!")
                elif choice == "9":
                    printLists()
                elif choice == "10":
                    limit()
                else:
                    break
            except:
                print("You did a dumb! Did you do it right?")

    """
    This function allows us to add singular integers to our list.
    """
    def addToList():
        print("Adding to a list! Great choice!")
        newItem = input("Type an integer here!    ")
        myList.append(int(newItem))

    """
    This function allows us to add more than one integer in any range to our list.
    """
    def addABunch():
        print("We're gonna add a bunch of integers here!")
        numToAdd = input("How many integers would you like to add?   ")
        numRange = input("And how high would you like these numbers to go?   ")
        for x in range(0, int(numToAdd)):
            myList.append(random.randint(0, int(numRange)))
        print("Your list is now complete.")

    """
    This function allows us to sort the list into numerical order.
    """
    def sortList(myList):
        for x in myList:
            if x not in unique_list:
                unique_list.append(x)
        unique_list.sort()
        showMe = input("Would you like to see the unique values in your list? Y/N   ")
        if showMe.lower() == "y":
            print(unique_list)
    """
    This function allows us to look for an integer at a specific index position.
    """
    def indexValues():
        print("At what index position do you want to search?")
        indexPos = input("Type an index position here:   ")
        print(myList[int(indexPos)])

    """
    This function allows us to look for an integer at a random index position.
    """
    def randomSearch():
        print("oH iM sO rAnDom!!!")
        print(myList[random.randint(0, len(myList)-1)])
        if len(unique_list) > 0:
            print(unique_list[random.randint(0, len(unique_list)-1)])
    """
    This function allows us to look for a certain number and look from beginning to end for that number.
    """
    def linearSearch():
        print("We're gonna check out each item one at a time in your list! This sucks.")
        searchItem = input("Whatcha lookin' for, pardner?   ")
        for x in range(len(myList)):
            if myList[x] == int(searchItem):
                print("Your item is at index position {}".format(x))

    """
    This function allws us to print and see the list.
    """
    def printLists():
        if len(unique_list) == 0:
            print(myList)
        else:
            whichOne = input("Which list do you want to see, sorted or un-sorted?   ")
            if whichOne.lower() == "sorted":
                print(unique_list)

    """
    This function searches for a certain number over and over until it finds it.
    """
    def recursiveBinarySearch(unique_list, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            if unique_list[mid] == x:
                print("You ding dang found your number at index position {}!".format(mid))
                return mid
            elif unique_list[mid] > x:
                return recursiveBinarySearch(unique_list, low, mid - 1, x)
            else:
                return recursiveBinarySearch(unique_list, mid + 1, high, x)
        else:
            print("Your number isn't here!")

    """
    This function searches for a certain number to check if it's in the list.
    """
    def iterativeBinarySearch(unique_list, x):
        low = 0
        high = len(unique_list)-1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if unique_list[mid] < x:
                low = mid + 1
            elif unique_list[mid] > x:
                high = mid - 1
            else:
                return mid
        return -1

    """
    This function limits the list to 10,000 integers. This is still experimental.
    """
    def limit():
        ar = map(int, input().split())
        ar = ar[:10000]
        if len(ar) > 10000:
            raise Exception("Hey, you can't go above 10,000 numbers, bud! Try taking some out!")

    if __name__ == "__main__":
        mainProgram()


if __name__ == "__main__":
    mainMenu()
    top.mainloop()
