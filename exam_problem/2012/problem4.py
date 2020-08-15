from game import Game

game = Game()

while True:
    ip = input()

    if ip == "end":
        break
    else:
        game.update_board(ip)
