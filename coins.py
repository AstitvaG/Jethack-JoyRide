from random import randint, sample
import defs

col_gf='\x1B[38;2;255;215;0m'
col_of='\x1b[38;2;255;165;0m'
col_ob='\x1b[48;2;255;165;0m'

coin0 = [col_gf,'','\u25D6',defs.fg+defs.bg]
coin1 = [col_gf,'','\u25D7',defs.fg+defs.bg]

class Coins:
    def __init__(self,freq,board):
        for p in range(defs.board_len//freq):
            ranx = randint(5,10)
            pos_x = sample(range(3+p*freq,freq*(p+1)-4),ranx)
            for x in pos_x:
                rany = randint(1,4)
                pos_y = sample(range(1,int(defs.rows)-1),rany)
                for y in pos_y:
                    x=int(x)
                    y=int(y)
                    try:
                        if defs.board_check[y][x] != 1 and defs.board_check[y][x-1]!=2 and defs.board_check[y][x+1] != 1:
                            board[y][x]=[coin0[0],board[y][x][1],coin0[2],coin0[3]]
                            board[y][x+1]=[coin1[0],board[y][x+1][1],coin1[2],coin1[3]]
                            defs.board_check[y][x]=2
                            defs.board_check[y][x+1]=2
                    except:
                        pass