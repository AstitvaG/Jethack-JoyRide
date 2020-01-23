import defs,elements
from random import randint
redf="\x1B[31m"
redb="\x1B[41m"
greyf='\x1b[38;2;100;100;100m'
greyb='\x1b[48;2;100;100;100m'


class Magnet(elements.Elements):
    __magnet = [
        [
            ['','',' ',defs.bg+defs.fg,-1,10],
            ['','',' ',defs.bg+defs.fg,-1,10],
            [redf,redb,'█',defs.bg+defs.fg,1,11],
            [redf,redb,'█',defs.bg+defs.fg,1,11],
            ['','',' ',defs.bg+defs.fg,-1,12],
            ['','',' ',defs.bg+defs.fg,-1,12]
        ],
        [
            [redf,redb,'█',defs.bg+defs.fg,1,13],
            [redf,redb,'█',defs.bg+defs.fg,1,13],
            [greyf,greyb,'█',defs.bg+defs.fg,1,14],
            [greyf,greyb,'█',defs.bg+defs.fg,1,14],
            [redf,redb,'█',defs.bg+defs.fg,1,15],
            [redf,redb,'█',defs.bg+defs.fg,1,15]
        ],
        [
            ['','',' ',defs.bg+defs.fg,-1,16],
            ['','',' ',defs.bg+defs.fg,-1,16],
            [redf,redb,'█',defs.bg+defs.fg,1,17],
            [redf,redb,'█',defs.bg+defs.fg,1,17],
            ['','',' ',defs.bg+defs.fg,-1,18],
            ['','',' ',defs.bg+defs.fg,-1,18]
        ]
    ]

    def __init__(self,freq,mgrange=3):
        for p in range(defs.board_len//freq):
            startx = randint(0,freq-1-len(self.__magnet[0]))+p*freq
            starty = randint(1+mgrange,int(defs.rows)-6-len(self.__magnet)-mgrange)

            for x in range(startx,startx+len(self.__magnet[0])):
                for y in range(starty,starty+len(self.__magnet)):
                    if(defs.board_check[y][x]==1):
                        break
                else:
                    break
            else:
                continue
            for x in range(startx,startx+len(self.__magnet[0])):
                for y in range(starty,starty+len(self.__magnet)):
                    defs.board_check[y][x]=self.__magnet[y-starty][x-startx][5]
            centerx = [startx+len(self.__magnet[0])//2-1,startx+len(self.__magnet[0])//2]
            centery = starty+len(self.__magnet)//2
            for x in range(startx-mgrange,startx+len(self.__magnet[0])+mgrange):
                for y in range(starty-mgrange,starty+len(self.__magnet)+mgrange):
                    try:
                        if defs.board_check[y][x] not in range(10,19) and defs.board_check[y][x]!=1:
                            if x<centerx[0] and y<centery:
                                defs.board_check[y][x]=19
                            elif x>centerx[1] and y<centery:
                                defs.board_check[y][x]=20
                            elif x<centerx[0] and y>centery:
                                defs.board_check[y][x]=21
                            elif x>centerx[1] and y>centery:
                                defs.board_check[y][x]=22
                            elif x in centerx and y<centery:
                                defs.board_check[y][x]=23
                            elif x<centerx[0] and y == centery:
                                defs.board_check[y][x]=24
                            elif x>centerx[1] and y == centery:
                                defs.board_check[y][x]=25
                            elif x in centerx and y>centery:
                                defs.board_check[y][x]=26
                    except:
                        pass
                            
    @staticmethod
    def fill_in(val):
        if val==10:
            return Magnet.__magnet[0][0][:5]
        elif val==11:
            return Magnet.__magnet[0][2][:5]
        elif val==12:
            return Magnet.__magnet[0][4][:5]
        elif val==13:
            return Magnet.__magnet[1][0][:5]
        elif val==14:
            return Magnet.__magnet[1][2][:5]
        elif val==15:
            return Magnet.__magnet[1][4][:5]
        elif val==16:
            return Magnet.__magnet[2][0][:5]
        elif val==17:
            return Magnet.__magnet[2][2][:5]
        elif val==18:
            return Magnet.__magnet[2][4][:5]
    
    @staticmethod
    def check_x(i,j):
        return defs.board_check[i][j] in range(10,19)

    @staticmethod
    def print_f(i,j):
        b = Magnet.fill_in(defs.board_check[i][j])
        if b[4]==-1:
            val = b[0]+defs.plain_board[i][j][1]+b[2]+b[3]
        else:
            val=b[0]+b[1]+b[2]+b[3]
        print(val,end="")