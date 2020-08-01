import numpy as np
from game import Game

arr = np.array([["○","×","○"],
                ["-","○","○"],
                ["×","×","-"]])


loc = list(input())

def input_tran(loc):

    if loc[1] == "A":
        loc[1] = 0
    elif loc[1] == "B":
        loc[1] = 1
    elif loc[1] == "C":
        loc[1] = 2

    if loc[0] == "1":
        loc[0] = 0
    elif loc[0] == "2":
        loc[0] = 1
    elif loc[0] == "3":
        loc[0] = 2
    return loc

loc = input_tran(loc)

game = Game(arr)

print(game.update_manual(loc[0],loc[1]))
