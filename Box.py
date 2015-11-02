class Box:
    startingX = 0
    startingY = 0
    isCompleted = False
    
    def __init__(self, x, y):
        self.startingX = x
        self.startingY = y
    
    def checkCompleted(self, board):
        for i in range(self.startingX, self.startingX + 3):
            for j in range(self.startingY, self.startingY + 3):
                if board[i][j] == 0:
                    return False
        self.isCompleted = True
        return True