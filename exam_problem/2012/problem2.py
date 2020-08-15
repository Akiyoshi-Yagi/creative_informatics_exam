from game import Game

game = Game()

while True:
    i = input()

    if i == "end":
        break
    else:
        game.update_board()
