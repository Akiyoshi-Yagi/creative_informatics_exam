from game import Game
import numpy as np

#マス目
n = int(input())
arr = np.empty((n,n),dtype=str)

for i in range(n):
    char = list(input())
    arr[i]= char


game = Game(arr)
game.show_board()


'''
○×○
×-×
○○-

'''
