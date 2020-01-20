from random import randint
import defs

class Powerup:
    def __init__(self,freq):
        for i in range(defs.board_len//freq):
            posx = randint(2,freq-2)
            posy = randint(4,int(defs.rows)-4)
            if defs.board_check[posy][posx+i*freq]!=0:
                i-=1
                continue
            defs.board_check[posy][posx+i*freq]=5
    @staticmethod
    def fill_in():
        b = ['\x1b[38;2;0;255;0m', '', '█', defs.bg+defs.fg, -1]
        return b
            