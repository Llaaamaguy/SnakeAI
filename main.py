import numpy as np
from Board import Board
import os
import time

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def main():
    board = Board(16)
    print(board)

    # A sequence to execute right, up, up, left, left, down
    time.sleep(0.5)
    board.snake_right()
    clearConsole()
    print(board)

    time.sleep(0.5)
    board.snake_up()
    clearConsole()
    print(board)

    time.sleep(0.5)
    board.snake_up()
    clearConsole()
    print(board)

    time.sleep(0.5)
    board.snake_left()
    clearConsole()
    print(board)

    time.sleep(0.5)
    board.snake_left()
    clearConsole()
    print(board)

    time.sleep(0.5)
    board.snake_down()
    clearConsole()
    print(board)


if __name__ == "__main__":
    main()
