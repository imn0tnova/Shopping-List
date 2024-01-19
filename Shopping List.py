#Nova and Alice
#1/10
#Shopping List

#Init
shoppingList = []
#Functions
def addTask():
    task = input("What task would you like to add?: ")
    shoppingList.append(task)
    print(shoppingList)
    editList()
def viewList():
    print(shoppingList)
    editList()
def removeTask():
    task2 = input("Which item would you like to remove?: ")
    shoppingList.remove(task2)
    print(shoppingList)
    editList()
def markComplete():
    ans = input("Select an item from the list to mark as complete: ")
    i = shoppingList.index(ans)
    shoppingList[i] = ans + " :X"
    print(shoppingList)
    editList()
def exitProgram():
    print("Thank you for using this program")
    quit()
def editList():
    ans = (input("Would you like to (1) add an item, (2) view your list, (3) mark an item as completed, (4) remove an item, (5) or exit the program? "))
    if ans == ("1"):
        addTask()
    elif ans == ("2"):
        viewList()
    elif ans == ("3"):
        markComplete()
    elif ans == ("4"):
        removeTask()
    elif ans == ("5"):
        exitProgram()
    else:
        print("Invalid response, try again")
        editList()

#Main
editList()