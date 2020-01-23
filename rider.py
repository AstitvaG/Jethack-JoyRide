import os
from clouds import add_element
from defs import reset_color,rows,columns,col_sb,col_sf
import defs,time,threading
from bullet import Bullet


class Rider:
    rider = [
             [['', '', ' ', '', -1], ['\x1b[38;2;224;172;172m', '\x1b[48;2;0;0;0m', '▅', '', 1]],
             [['\x1b[38;2;0;0;0m', '', '▉', '', -1],    ['\x1b[38;2;0;0;139m', '', '█', '', -1]],
             [['', '', ' ', '', -1],  ['\x1b[38;2;0;0;0m', '', '▛', '', -1]]
            ]
    __rider_normal = [
             [['', '', ' ', '', -1], ['\x1b[38;2;224;172;172m', '\x1b[48;2;0;0;0m', '▅', '', 1]],
             [['\x1b[38;2;0;0;0m', '', '▉', '', -1],    ['\x1b[38;2;0;0;139m', '', '█', '', -1]],
             [['', '', ' ', '', -1],  ['\x1b[38;2;0;0;0m', '', '▛', '', -1]]
            ]
    __rider_fly = [
             [['', '', ' ', '', -1], ['\x1b[38;2;224;172;172m', '\x1b[48;2;0;0;0m', '▅', '', 1]],
             [['\x1b[38;2;0;0;0m', '', '▉', '', -1],    ['\x1b[38;2;0;0;139m', '', '█', '', -1]],
             [['\x1b[38;2;252;186;3m', '', '▘', '', -1],  ['\x1b[38;2;0;0;0m', '', '▛', '', -1]]
            ]
    __rider_flyback = [
             [['', '', ' ', '', -1], ['\x1b[38;2;224;172;172m', '\x1b[48;2;0;0;0m', '▅', '', 1]],
             [['\x1b[38;2;0;0;0m', '', '▉', '', -1],    ['\x1b[38;2;0;0;139m', '', '█', '', -1]],
             [['\x1b[38;2;252;186;3m', '', '▘', '', -1],  ['\x1b[38;2;0;0;0m', '', '▜', '', -1]]
            ]

    __sheild_rider = [
                [
                    [col_sf,'','▗','',-1],
                    [col_sf,col_sb,'█','',1],
                    [col_sf,col_sb,'█','',1],
                    [col_sf,'','▖','',-1]
                ],
                [
                    [col_sf,col_sb,'█','',1],
                    ['', '', ' ', '', -1],
                    ['\x1b[38;2;224;172;172m', '\x1b[48;2;0;0;0m', '▅', '', 1],
                    [col_sf,col_sb,'█','',1]
                ],
                [
                    [col_sf,col_sb,'█','',1],
                    ['\x1b[38;2;0;0;0m', '', '▉', '', 1],
                    ['\x1b[38;2;0;0;139m', '', '█', '', 1],
                    [col_sf,col_sb,'█','',1]
                ],
                [
                    [col_sf,col_sb,'█','',1],
                    ['\x1b[38;2;252;186;3m', '', '▘', '', -1],
                    ['\x1b[38;2;0;0;0m', '', '▛', '', -1],
                    [col_sf,col_sb,'█','',1]
                ],
                [
                    [col_sf,'','▝','',-1],
                    [col_sf,col_sb,'█','',1],
                    [col_sf,col_sb,'█','',1],
                    [col_sf,'','▘','',-1]
                ],
            ]
    _isSheilded=False
    __isSheildPossible=True
    def sheild_toggle(self):
        self.__isSheildPossible=False
        time.sleep(60)
        self.__isSheildPossible=True
    def activate_sheild(self):
        self.change_rider(3)
        self._isSheilded=True
        time.sleep(10)
        self._isSheilded=False
        self.change_rider(0)
    def sheild(self):
        if self.__isSheildPossible:
            thread1 = threading.Thread(target=self.sheild_toggle, daemon=True)
            thread1.start()
            thread2 = threading.Thread(target=self.activate_sheild, daemon=True)
            thread2.start()

    def gen_rider(self):
        row=list()
        row.append(add_element(cont=1,element=" ")+[-1])
        row.append(add_element(r1=224,g1=172,b1=172,bx=1,element="\u2585")+[1])
        self.rider.append(row)
        row = list()
        row.append(add_element(bx=0,element="\u2589")+[-1])
        row.append(add_element(bx=0,b1=139,element="\u2588")+[-1])
        self.rider.append(row)
        row = list()
        row.append(add_element(r1=252,g1=186,b1=3,bx=0,element="\u2598")+[-1])
        row.append(add_element(bx=0,element="\u259B")+[-1])
        self.rider.append(row)

    def change_rider(self,val):
        if val==1:
            self.rider=self.__rider_fly
        elif val==2:
            self.rider=self.__rider_flyback
        elif val==0:
            self.rider=self.__rider_normal
        elif val==3:
            self.rider=self.__sheild_rider
            self.xpos_left+=1
            self.ypos_top+=1


    def __init__(self,xpos_start=4,ypos_start=int(rows)//2,addx=rider):
        # self.gen_rider()
        self.xpos_left = xpos_start
        self.ypos_top = ypos_start
        self.art_areax=range(self.xpos_left,self.xpos_left+len(addx[0]))
        self.art_areay=range(self.ypos_top,self.ypos_top+len(addx))
        # self.print_rider()

    def move(self,chbuff,x=False,val=-1):
        if chbuff == 'w':
            self.ypos_top -= 4 if (val==-1) else val
            if self.ypos_top<1:
                self.ypos_top=1
            if not self._isSheilded:    
                self.change_rider(1)
        elif chbuff == 's':
            self.ypos_top += 2 if val==-1 else val
            if self.ypos_top>int(rows)-1-len(self.rider):
                self.ypos_top=int(rows)-1-len(self.rider)
        elif chbuff == 'a':
            self.xpos_left -= 1 if val==-1 else val
            if self.xpos_left<0:
                self.xpos_left=0
            if x==False and not self._isSheilded:
                self.change_rider(2)
        elif chbuff == 'd':
            self.xpos_left += 3 if val==-1 else val
            if self.xpos_left>int(columns)-2:
                self.xpos_left=int(columns)-2
            if not self._isSheilded:    
                self.change_rider(1)
        self.art_areax=range(self.xpos_left,self.xpos_left+len(self.rider[0]))
        self.art_areay=range(self.ypos_top,self.ypos_top+len(self.rider))
    
    def mgcheck_pos(self,posx,posy):
        a = defs.board_check[posy][posx]
        if a in [10,16,19,21,24]:
            self.move('d',val=1)
        if a in [12,18,20,22,25]:
            self.move('a',val=1)
        if a in [10,12,19,20,23]:
            self.move('s',val=1)
        if a in [16,18,21,22,26]:
            self.move('w',val=2)
        if a in range(10,27):
            defs.down=0

    def check_pos(self):
        for i in self.art_areay:
            for j in self.art_areax:
                if(j+defs.board_start-1>defs.board_len-1): 
                    return
                if defs.board_check[i][j+defs.board_start-1] in [1,30] and not self._isSheilded:
                    defs.livesleft-=1
                    if defs.board_check[i][j+defs.board_start-1]==1:
                        Bullet.clearArcs(j+defs.board_start-1,i)
                    return
                elif defs.board_check[i][j+defs.board_start-1] in [1,30]:
                    self._isSheilded=False
                    Bullet.clearArcs(j+defs.board_start-1,i)
                    return
                if defs.board_check[i][j+defs.board_start] == 2:
                    defs.board_check[i][j+defs.board_start]=0
                    defs.board_check[i][j+defs.board_start-1]=0
                    defs.board_check[i][j+defs.board_start+1]=0
                    defs.coinsCollected+=1
                    return
                if defs.board_check[i][j+defs.board_start] == 5:
                    defs.board_check[i][j+defs.board_start]=0
                    defs.speed/=2
                    return
        self.mgcheck_pos(self.art_areax[0]+defs.board_start,self.art_areay[0])