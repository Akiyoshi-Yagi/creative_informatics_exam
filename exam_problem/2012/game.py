import random

class Game:
    def __init__(self):
        self.board = [["|","-","-","-","-","-","-","-","|"],
                      ["|"," "," "," "," "," "," "," ","|"],
                      ["|"," "," "," "," "," "," "," ","|"],
                      ["|"," "," "," "," "," "," "," ","|"],
                      ["|"," "," "," "," "," "," "," ","|"],
                      ["|"," "," "," "," "," "," "," ","|"],
                      ["|"," "," "," "," "," "," "," ","|"],
                      ["|"," "," "," "," "," "," "," ","|"],
                      ["|"," "," "," "," "," "," "," ","|"],
                      ["|"," "," "," "," "," "," "," ","|"],
                      ["|"," "," "," "," "," "," "," ","|"],
                      ["|"," "," "," "," "," "," "," ","|"],
                      ["|"," "," "," "," "," "," "," ","|"],
                      ["|"," "," "," "," "," "," "," ","|"],
                      ["|",".",".",".","X",".",".",".","|"],]

        self.boss_loc = [0,4]
        self.is_enemy = False
        self.enemy_loc = [0,0]
        self.gan_loc = [14, 4]
        self.ball_loc = []
        self.enemy_direction = 1 #1が右むき,-1が左むき
        self.is_ball = False
        self.score = 0

    def show_board(self):
        if self.is_enemy:
            x, y = self.enemy_loc
            self.board[x][y] = "o"
        for i in self.ball_loc:
            x, y = i
            self.board[x][y] = "e"
        z, w = self.boss_loc
        self.board[z][w] = "V"
        p, q = self.gan_loc
        self.board[p][q] = "X"
        for l in self.board:
            print(" ".join(l))

    def ctl_enemy(self):
        if not self.is_enemy:
            self.create_enemy()
        elif "o" in self.board[14]:
            print("消去")
            self.delete_enemy()
        else:
            if "o" in [self.board[i][0] for i in range(15)] or "o" in [self.board[i][8] for i in range(15)]:
                self.enemy_direction *= -1
            self.move_enemy()

    def move_enemy(self):
        x, y = self.enemy_loc
        if y == 0 or y == 8:
            self.board[x][y] = "|"
        elif x == 0:
            self.board[x][y] = "-"
        elif self.enemy_loc == self.gan_loc:
            self.board[x][y] = "X"
        elif x == 14:
            self.board[x][y] = "."
        else:
            self.board[x][y] = " "

        if self.enemy_direction == 1:
            self.enemy_loc = [x+1,y+1]
        elif self.enemy_direction == -1:
            self.enemy_loc = [x+1,y-1]

    def create_enemy(self):
        i = random.randint(1,7)
        z, w = self.boss_loc
        self.board[z][w] = "-"
        self.enemy_loc = [0,i]
        self.boss_loc = [0,i]
        self.is_enemy = True

    def delete_enemy(self):
        x, y = self.enemy_loc
        self.board[x][y] = "."
        self.is_enemy = False

    def ctl_gan(self):
        for i in self.ball_loc:
            x, y = i
            self.board[x][y] = " "
            if x == 0:
                self.ball_loc.remove(i)
                self.board[x][y] = "-"

            else:
                i[0] -= 1


    def create_ball(self):
        if len(self.ball_loc) >=  2:
            print("これ以上発射できません")
        else:
            x, y = self.gan_loc
            self.ball_loc.append([x-1, y])

    def move_left(self):
        x, y = self.gan_loc
        self.board[x][y] = "."
        if self.gan_loc[1] >= 2:
            self.gan_loc[1] -= 1
        else:
            print("左に動けません")
    def move_right(self):
        x, y = self.gan_loc
        self.board[x][y] = "."
        if self.gan_loc[1] <= 6:
            self.gan_loc[1] += 1
        else:
            print("右に動けません")



    def update_board(self, ip):
        if ip == "i":
            print("発射")
            self.create_ball()
        elif ip == "j":
            self.move_left()
        elif ip == "l":
            self.move_right()
        self.ctl_enemy()
        self.ctl_gan()
        for i in self.ball_loc:
            x,y = i
            z,w = self.enemy_loc
            if x == z and y == w:
                self.ball_loc.remove(i)
                self.enemy_loc = []
                self.is_enemy = False
                self.enemy_direction = 1
                self.score += 1
        self.show_board()
        print(self.score)



