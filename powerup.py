from random import randint
import defs,elements

class Powerup(elements.Elements):
    def __init__(self,freq):
        for i in range(defs.board_len//freq):
            posx = randint(2,freq-2)
            posy = randint(4,int(defs.rows)-4)
            if defs.board_check[posy][posx+i*freq]!=0:
                i-=1
                continue
            defs.board_check[posy][posx+i*freq]=5
    @staticmethod
    def fill_in(val):
        b = ['\x1b[38;2;0;255;0m', '', '█', defs.bg+defs.fg, -1]
        return b

    @staticmethod
    def check_x(i,j):
        try:
            return defs.board_check[i][j]==5
        except:
            return False
    @staticmethod
    def print_f(i,j):
        b = Powerup.fill_in(1)
        print(b[0]+b[1]+b[2]+b[3],end="")            