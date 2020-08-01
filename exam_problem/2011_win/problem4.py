from game import Game
import numpy as np
import time

arr = np.array([["-","-","-"],
                ["-","-","-"],
                ["-","-","-"]])

i = 0
game = Game(arr)
while game.vacant != 0 and game.isEnd == False:
    i += 1
    game.update_auto()
    print(str(i)+"------------")
    time.sleep(1)
if game.vacant == 0 and game.isEnd == False:
    print("引き分け")

