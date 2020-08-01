import numpy as np
import random

class Game:

    def __init__(self, arr):
        self.circle = 0
        self.cross = 0
        self.vacant = 0
        self.board = arr
        self.isEnd = False
        for x in arr:
            for y in x:
                if y == "○":
                    self.circle += 1
                elif y == "×":
                    self.cross += 1
                else:
                    self.vacant += 1

    def show_board(self):

        for line in self.board:
            for index, char in enumerate(line):
                if index == len(line) - 1:
                    print(char)
                else:
                    print(char, end="")

    def update_manual(self,x,y):
        if self.vacant == 0:
            print("空きがありません")
        else:
            if self.board[x][y]  in ["○","×"]:
                return "そのマスは埋まっています"
            if self.circle == self.cross:
                self.board[x][y] = "○"
                self.circle += 1
                self.vacant -= 1
            else:
                self.board[x][y] = "×"
                self.cross += 1
                self.vacant -= 1

            if self.check_game():
                self.isEnd =True
                return self.check_game()
            return self.show_board()


    def check_game(self):
        for char in ["○","×"]:
            for i in range(3):
                if (self.board[i] == np.array([char] * 3)).all() \
                        or all([self.board[0][i]==char, self.board[1][i]==char, self.board[2][i]==char]):
                    return char
            if all([self.board[j][j] == char for j in range(3)]) \
                    or all([self.board[2][0] == char, self.board[1][1]==char, self.board[0][2]==char]):
                return char
            else:
                pass
        return False

    def update_auto(self):

        x, y = self.random_select()
        if self.vacant == 0:
            print("終了")
        else:
            if self.circle == self.cross:
                self.board[x][y] = "○"
                self.circle += 1
                self.vacant -= 1
            else:
                self.board[x][y] = "×"
                self.cross += 1
                self.vacant -= 1

            result =  self.check_game()

            if result in ["○", "×"]:
                self.isEnd = True
                print(self.exit())
                print("勝者:"+result)
            return self.show_board()



    def random_select(self):
        l = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "-":
                    l.append([i,j])
        r_loc = random.choice(l)
        return r_loc

    def exit(self):
        return self.show_board()
