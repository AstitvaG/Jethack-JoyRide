from random import randint
import defs

class Enemy:
    
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