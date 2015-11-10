from __future__ import print_function
from Box import *
boxes = []
absentNumbers = 0
board = [
    [6,0,0,1,0,8,0,0,3],
    [0,2,0,0,4,0,0,9,0],
    [8,0,3,0,0,5,4,0,0],
    [5,0,4,6,0,7,0,0,9],
    [0,3,0,0,0,0,0,5,0],
    [7,0,0,8,0,3,1,0,2],
    [0,0,1,7,0,0,9,0,6],
    [0,8,0,0,3,0,0,2,0],
    [3,0,2,9,0,4,0,0,5]
]
  
def generateBoxes():
    for i in range(0,7,3):
        for j in range(0,7,3):
            boxes.append(Box(i, j))

def findAbsentNumbers():
    counter = 0
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 0:
                counter +=1
    return counter

def solveSudoku():
    global absentNumbers
    possibleNumbers = []
    while(absentNumbers != 0):
        for box in boxes:
            for number in range(1,10):
                for i in range(box.startingX, box.startingX + 3):
                    for j in range(box.startingY, box.startingY + 3):
                        if board[i][j] == 0:
                            if lookOwnRow(i, number) == False and lookOwnColumn(j, number) == False and lookOwnBox(box.startingX, box.startingY, number) == False:
                                #print(box.startingX, box.startingY)
                                possibleNumbers.append({"x" : i, "y" : j, "number" : number})
                if len(possibleNumbers) == 1:
                    printBoard()
                    print ("---------********----------")
                    board[possibleNumbers[0]["x"]][possibleNumbers[0]["y"]] = possibleNumbers[0]["number"]
                    executeOwnColumn(possibleNumbers[0]["y"])
                    executeOwnRow(possibleNumbers[0]["x"])
                    absentNumbers -=1
                possibleNumbers = []
          
    printBoard()
    
def printBoard():
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            print (board[i][j], end=" ")
        print ()
        
def executeOwnColumn(y):
    global absentNumbers
    numbers = [1,2,3,4,5,6,7,8,9]
    for i in range(0,len(board)):
        if board[i][y] != 0:
            numbers.remove(board[i][y])
        continue
    if len(numbers) == 1:
        for i in range(0, len(board)):
            if board[i][y] == 0:
                board[i][y] = numbers.pop()
                absentNumbers -=1
def executeOwnRow(x):
    global absentNumbers
    numbers = [1,2,3,4,5,6,7,8,9]
    for j in range(0, len(board)):
        if board[x][j] != 0:
            numbers.remove(board[x][j])
    if len(numbers) == 1:
        for i in range(0, len(board)):
            if board[x][i] == 0:
                board[x][i] = numbers.pop()
                absentNumbers -=1
    
def lookOwnBox(x, y, number):
    for i in range(x, x + 3):
        for j in range(y , y + 3):
            if board[i][j] == number:
                return True
    return False

def lookOwnRow(row, number):
    for i in range(0,9):
        if board[row][i] == number:
            return True
    return False

def lookOwnColumn(column, number):
    for i in range(0,9):
        if board[i][column] == number:
            return True
    return False
absentNumbers = findAbsentNumbers()
print (absentNumbers)
generateBoxes()
solveSudoku()
