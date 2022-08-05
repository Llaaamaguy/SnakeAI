import numpy as np
from Board import Board
import os
import time

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def main():
    board = Board(16)
    print(board)
    """
    gameState = True
    while gameState:
        print(f"Move choices: {board.move_choices()}")
        move = input("Enter a move. Left (l), Right (r), Down (d), or Up (u):  ")
        match move:
            case "l":
                res = board.snake_left()
            case "r":
                res = board.snake_right()
            case "d":
                res = board.snake_down()
            case "u":
                res = board.snake_up()
            case other:
                raise ValueError("Incorrect input")
        clearConsole()
        print(board)
        if res == "GameFail":
            gameState = False
    print("Game Over")
    """

    res = True
    while res:
        res = board.algorithm_move()
        time.sleep(0.5)
        clearConsole()
        print(board)

        if res == "GameFail":
            print("GAME FAIL")
            res = False
    print("Game Over")


if __name__ == "__main__":
    main()
