import numpy as np
from Cell import Cell
import random


# Since the board is a nparray, index by board[y][x]
class Board:
    def __init__(self, size):
        # Initial variables
        self.score = 0
        self.length = 3
        self.size = size

        # Generates the empty board
        self.board = np.array([[Cell("Empty") if 0 < i < size - 1 else Cell("Wall") for i in range(size)] if 0 < j < size - 1 else [Cell("Wall") for _ in range(size)] for j in range(size)])

        # Place the initial snake on the board
        self.headPos = (int(round(size/2)), int(round(size/2)))
        self.board[self.headPos[0]][self.headPos[1]] = Cell("Body head")
        self.bodyPosAll = [self.headPos]
        for i in range(self.length-1):
            self.board[self.headPos[0]][self.headPos[1]-(i+1)] = Cell("Body body") if i+1 < self.length-1 else Cell("Body tail")
            self.bodyPosAll.append((self.headPos[0], self.headPos[1]-(i+1)))
        self.tailPos = self.bodyPosAll[-1]

        # Place the apple on the board
        aPosY = 0
        aPosX = 0
        while self.board[aPosY][aPosX].cellType != "Empty":
            aPosY = random.randint(1, size)
            aPosX = random.randint(1, size)
        self.applePos = (aPosY, aPosX)
        self.board[aPosY][aPosX] = Cell("Apple")

    def __str__(self):
        return str(self.board)

    def __repr__(self):
        return f"Board Object of size {self.size}x{self.size}"

    def snake_right(self):
        desiredCell = self.board[self.headPos[0]][self.headPos[1]+1]
        if desiredCell.is_hard():
            return "GameFail"
        if desiredCell.cellType == "Apple":
            self.length += 1
            self.board[self.headPos[0]][self.headPos[1]] = Cell("Body")
            self.board[self.headPos[0]][self.headPos[1]+1] = Cell("Body head")
            self.headPos = (self.headPos[0], self.headPos[1]+1)
            self.bodyPosAll.insert(0, self.headPos)
            return True
        self.board[self.headPos[0]][self.headPos[1]] = Cell("Body")
        self.board[self.headPos[0]][self.headPos[1] + 1] = Cell("Body head")
        self.headPos = (self.headPos[0], self.headPos[1] + 1)
        self.board[self.tailPos[0]][self.tailPos[1]] = Cell("Empty")
        self.bodyPosAll.pop(-1)
        self.tailPos = self.bodyPosAll[-1]
        self.bodyPosAll.insert(0, self.headPos)
        return True

    def snake_up(self):
        desiredCell = self.board[self.headPos[0] - 1][self.headPos[1]]
        if desiredCell.is_hard():
            return "GameFail"
        if desiredCell.cellType == "Apple":
            self.length += 1
            self.board[self.headPos[0]][self.headPos[1]] = Cell("Body")
            self.board[self.headPos[0]-1][self.headPos[1]] = Cell("Body head")
            self.headPos = (self.headPos[0]-1, self.headPos[1])
            self.bodyPosAll.insert(0, self.headPos)
            return True
        self.board[self.headPos[0]][self.headPos[1]] = Cell("Body")
        self.board[self.headPos[0]-1][self.headPos[1]] = Cell("Body head")
        self.headPos = (self.headPos[0]-1, self.headPos[1])
        self.board[self.tailPos[0]][self.tailPos[1]] = Cell("Empty")
        self.bodyPosAll.pop(-1)
        self.tailPos = self.bodyPosAll[-1]
        self.bodyPosAll.insert(0, self.headPos)
        return True

    def snake_left(self):
        desiredCell = self.board[self.headPos[0]][self.headPos[1]-1]
        if desiredCell.is_hard():
            return "GameFail"
        if desiredCell.cellType == "Apple":
            self.length += 1
            self.board[self.headPos[0]][self.headPos[1]] = Cell("Body")
            self.board[self.headPos[0]][self.headPos[1]-1] = Cell("Body head")
            self.headPos = (self.headPos[0], self.headPos[1]-1)
            self.bodyPosAll.insert(0, self.headPos)
            return True
        self.board[self.headPos[0]][self.headPos[1]] = Cell("Body")
        self.board[self.headPos[0]][self.headPos[1]-1] = Cell("Body head")
        self.headPos = (self.headPos[0], self.headPos[1]-1)
        self.board[self.tailPos[0]][self.tailPos[1]] = Cell("Empty")
        self.bodyPosAll.pop(-1)
        self.tailPos = self.bodyPosAll[-1]
        self.bodyPosAll.insert(0, self.headPos)
        return True

    def snake_down(self):
        desiredCell = self.board[self.headPos[0] + 1][self.headPos[1]]
        if desiredCell.is_hard():
            return "GameFail"
        if desiredCell.cellType == "Apple":
            self.length += 1
            self.board[self.headPos[0]][self.headPos[1]] = Cell("Body")
            self.board[self.headPos[0]+1][self.headPos[1]] = Cell("Body head")
            self.headPos = (self.headPos[0]+1, self.headPos[1])
            self.bodyPosAll.insert(0, self.headPos)
            return True
        self.board[self.headPos[0]][self.headPos[1]] = Cell("Body")
        self.board[self.headPos[0]+1][self.headPos[1]] = Cell("Body head")
        self.headPos = (self.headPos[0]+1, self.headPos[1])
        self.board[self.tailPos[0]][self.tailPos[1]] = Cell("Empty")
        self.bodyPosAll.pop(-1)
        self.tailPos = self.bodyPosAll[-1]
        self.bodyPosAll.insert(0, self.headPos)
        return True
