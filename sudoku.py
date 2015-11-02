from Box import *
boxes = []

board = [
    [3,0,0,2,4,0,0,0,0],
    [0,4,0,0,0,0,0,5,3],
    [1,8,9,6,3,5,4,0,0],
    [0,0,0,0,8,0,2,0,0],
    [0,0,7,4,9,6,8,0,1],
    [8,9,3,1,5,0,6,0,4],
    [0,0,1,9,2,0,5,0,0],
    [2,0,0,3,0,0,7,4,0],
    [9,6,0,5,0,0,3,0,2]
]



        
        
def generateBoxes():
    for i in range(0,7,3):
        for j in range(0,7,3):
            boxes.append(Box(i, j))

def solveSudoku():
    for box in boxes:
        for i in range(box.startingX, box.startingX + 3):
            for j in range(box.startingY, box.startingY + 3):
                if board[i][j] == 0:
                    for k in range(1,10):
                        
                    
def executeOwnColumn(y):
    numbers = [1,2,3,4,5,6,7,8,9]
    for i in range(0,len(board)):
        if board[i][y] != 0:
            numbers.remove(board[i][y])
        continue
    return numbers

def executeOwnRow(x):
    numbers = [1,2,3,4,5,6,7,8,9]
    for j in range(0, len(board)):
        if board[x][j] != 0:
            print board[x][j]
            numbers.remove(board[x][j])
    return numbers
        
def lookOwnBox(x, y, number):
    for i in range(x, x + 3):
        for j in range(y , y + 3):
            if board[i][j] == number:
                return True
    return False

def lookOwnRow(row ,number):
    for i in range(0,9):
        if board[row][i] == number:
            return True
    return False

def lookOwnColumn(column, number):
    for i in range(0,9):
        if board[i][column] == number:
            return True
    return False

generateBoxes()