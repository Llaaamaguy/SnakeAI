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
        self.lastMove = None

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
        self.__place_apple()

    def __str__(self):
        return str(self.board)

    def __repr__(self):
        return f"Board Object of size {self.size}x{self.size}"

    def __place_apple(self):
        aPosY = 0
        aPosX = 0
        while self.board[aPosY][aPosX].cellType != "Empty":
            aPosY = random.randint(1, self.size-1)
            aPosX = random.randint(1, self.size-1)
        self.applePos = (aPosY, aPosX)
        self.board[aPosY][aPosX] = Cell("Apple")

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
            self.__place_apple()
            self.lastMove = "r"
            return True
        self.board[self.headPos[0]][self.headPos[1]] = Cell("Body")
        self.board[self.headPos[0]][self.headPos[1] + 1] = Cell("Body head")
        self.headPos = (self.headPos[0], self.headPos[1] + 1)
        self.board[self.tailPos[0]][self.tailPos[1]] = Cell("Empty")
        self.bodyPosAll.pop(-1)
        self.tailPos = self.bodyPosAll[-1]
        self.bodyPosAll.insert(0, self.headPos)
        self.lastMove = "r"
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
            self.__place_apple()
            self.lastMove = "u"
            return True
        self.board[self.headPos[0]][self.headPos[1]] = Cell("Body")
        self.board[self.headPos[0]-1][self.headPos[1]] = Cell("Body head")
        self.headPos = (self.headPos[0]-1, self.headPos[1])
        self.board[self.tailPos[0]][self.tailPos[1]] = Cell("Empty")
        self.bodyPosAll.pop(-1)
        self.tailPos = self.bodyPosAll[-1]
        self.bodyPosAll.insert(0, self.headPos)
        self.lastMove = "u"
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
            self.__place_apple()
            self.lastMove = "l"
            return True
        self.board[self.headPos[0]][self.headPos[1]] = Cell("Body")
        self.board[self.headPos[0]][self.headPos[1]-1] = Cell("Body head")
        self.headPos = (self.headPos[0], self.headPos[1]-1)
        self.board[self.tailPos[0]][self.tailPos[1]] = Cell("Empty")
        self.bodyPosAll.pop(-1)
        self.tailPos = self.bodyPosAll[-1]
        self.bodyPosAll.insert(0, self.headPos)
        self.lastMove = "l"
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
            self.__place_apple()
            self.lastMove = "d"
            return True
        self.board[self.headPos[0]][self.headPos[1]] = Cell("Body")
        self.board[self.headPos[0]+1][self.headPos[1]] = Cell("Body head")
        self.headPos = (self.headPos[0]+1, self.headPos[1])
        self.board[self.tailPos[0]][self.tailPos[1]] = Cell("Empty")
        self.bodyPosAll.pop(-1)
        self.tailPos = self.bodyPosAll[-1]
        self.bodyPosAll.insert(0, self.headPos)
        self.lastMove = "d"
        return True

    def move_choices(self):
        if self.lastMove:
            upCell = self.board[self.headPos[0] - 1][self.headPos[1]]
            downCell = self.board[self.headPos[0] + 1][self.headPos[1]]
            leftCell = self.board[self.headPos[0]][self.headPos[1]-1]
            rightCell = self.board[self.headPos[0]][self.headPos[1]+1]
            choices = {"u": upCell, "d": downCell, "l": leftCell, "r": rightCell}
            inverses = {"u": "d", "d": "u", "l": "r", "r": "l"}
            match self.lastMove:
                case "u":
                    del choices[inverses["u"]]
                case "d":
                    del choices[inverses["d"]]
                case "l":
                    del choices[inverses["l"]]
                case "r":
                    del choices[inverses["r"]]

            return list(choices.keys())
        return None
