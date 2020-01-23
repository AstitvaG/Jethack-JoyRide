from random import randint
import defs,elements

class Enemy(elements.Elements):
    
    def __init__(self,freq):
        for i in range(defs.board_len//freq):
            posx = randint(6,freq-6)
            posy = int(defs.rows)-4
            defs.board_check[posy][posx+i*freq]=8
            defs.board_check[posy+1][posx+i*freq]=7
            defs.board_check[posy+2][posx+i*freq]=6
    @staticmethod
    def fill_in(val):
        r=str(randint(0,255))
        g=str(randint(0,255))
        b=str(randint(0,255))
        enemy =  [
            ['\x1b[38;2;224;172;172m', '\x1b[48;2;0;0;0m', '▅', defs.bg+defs.fg, 1],
            # ['\x1b[38;2;0;0;0m', '', '█', defs.bg+defs.fg, -1],
            ['\x1b[38;2;'+r+';'+g+';'+b+'m', '', '█', defs.bg+defs.fg, -1],
            ['\x1b[38;2;0;0;0m', '\x1b[48;2;105;105;105m', '▋', defs.bg+defs.fg, 1]
        ]
        return enemy[8-val]

    @staticmethod
    def check_x(i,j):
        if j+defs.board_start-defs.enemyrelpos<defs.board_len-1 and\
            defs.board_check[i][j-defs.enemyrelpos] in [6,7,8]:
            return True
        else:
            return False

    @staticmethod
    def print_f(i,j):
        b = Enemy.fill_in(defs.board_check[i][j-defs.enemyrelpos])
        print(b[0]+b[1]+b[2]+b[3],end="")