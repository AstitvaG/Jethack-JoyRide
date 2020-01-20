import os
from clouds import add_element
from defs import reset_color,rows,columns,col_sb,col_sf
import defs,time,threading
from stats import Stats
from bullet import Bullet

game_stats=Stats()

def gc(c="\u2588",r=0,g=0,b=0,f=1,e=1,c1="",r1=0,g1=0,b1=0):
    ret_str = "\x1b[38;2;"+str(r)+";"+str(g)+";"+str(b)+"m"+str(c)
    if f==0:
        ret_str = "\x1b[38;2;"+str(r)+";"+str(g)+";"+str(b)+"m"+str(c1)
        ret_str += "\x1b[48;2;"+str(r1)+";"+str(g1)+";"+str(b1)+"m"+str(c)
    if e==1:
        ret_str+=reset_color
    return ret_str

class Rider:
    rider = [
             [['', '', ' ', '', -1], ['\x1b[38;2;224;172;172m', '\x1b[48;2;0;0;0m', '▅', '', 1]],
             [['\x1b[38;2;0;0;0m', '', '▉', '', -1],    ['\x1b[38;2;0;0;139m', '', '█', '', -1]],
             [['', '', ' ', '', -1],  ['\x1b[38;2;0;0;0m', '', '▛', '', -1]]
            ]
    rider_normal = [
             [['', '', ' ', '', -1], ['\x1b[38;2;224;172;172m', '\x1b[48;2;0;0;0m', '▅', '', 1]],
             [['\x1b[38;2;0;0;0m', '', '▉', '', -1],    ['\x1b[38;2;0;0;139m', '', '█', '', -1]],
             [['', '', ' ', '', -1],  ['\x1b[38;2;0;0;0m', '', '▛', '', -1]]
            ]
    rider_fly = [
             [['', '', ' ', '', -1], ['\x1b[38;2;224;172;172m', '\x1b[48;2;0;0;0m', '▅', '', 1]],
             [['\x1b[38;2;0;0;0m', '', '▉', '', -1],    ['\x1b[38;2;0;0;139m', '', '█', '', -1]],
             [['\x1b[38;2;252;186;3m', '', '▘', '', -1],  ['\x1b[38;2;0;0;0m', '', '▛', '', -1]]
            ]
    rider_flyback = [
             [['', '', ' ', '', -1], ['\x1b[38;2;224;172;172m', '\x1b[48;2;0;0;0m', '▅', '', 1]],
             [['\x1b[38;2;0;0;0m', '', '▉', '', -1],    ['\x1b[38;2;0;0;139m', '', '█', '', -1]],
             [['\x1b[38;2;252;186;3m', '', '▘', '', -1],  ['\x1b[38;2;0;0;0m', '', '▜', '', -1]]
            ]

    sheild_rider = [
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
    _isSheildPossible=True
    def sheild_toggle(self):
        self._isSheildPossible=False
        time.sleep(60)
        self._isSheildPossible=True
    def activate_sheild(self):
        self.change_rider(3)
        self._isSheilded=True
        time.sleep(10)
        self._isSheilded=False
        self.change_rider(0)
    def sheild(self):
        if self._isSheildPossible:
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
            self.rider=self.rider_fly
        elif val==2:
            self.rider=self.rider_flyback
        elif val==0:
            self.rider=self.rider_normal
        elif val==3:
            self.rider=self.sheild_rider
            self.xpos_left+=1
            self.ypos_top+=1


    def __init__(self):
        # self.gen_rider()
        self.xpos_left = 4
        self.ypos_top = int(rows)//2
        self.art_areax=range(self.xpos_left,self.xpos_left+len(self.rider[0]))
        self.art_areay=range(self.ypos_top,self.ypos_top+len(self.rider))
        # self.print_rider()

    def move(self,chbuff,x=False):
        if chbuff == 'w':
            self.ypos_top -= int(4*(defs.def_speed//defs.speed))
            if self.ypos_top<-1:
                self.ypos_top=-1
            if not self._isSheilded:    
                self.change_rider(1)
        elif chbuff == 's':
            self.ypos_top += int(2*(defs.def_speed//defs.speed))
            if self.ypos_top>int(rows)-1-len(self.rider):
                self.ypos_top=int(rows)-1-len(self.rider)
        elif chbuff == 'a':
            self.xpos_left -= int(1*(defs.def_speed//defs.speed))
            if self.xpos_left<0:
                self.xpos_left=0
            if x==False and not self._isSheilded:
                self.change_rider(2)
        elif chbuff == 'd':
            self.xpos_left += int(3*(defs.def_speed//defs.speed))
            if self.xpos_left>int(columns)-2:
                self.xpos_left=int(columns)-2
            if not self._isSheilded:    
                self.change_rider(1)
        self.art_areax=range(self.xpos_left,self.xpos_left+len(self.rider[0]))
        self.art_areay=range(self.ypos_top,self.ypos_top+len(self.rider))
       
    def check_pos(self):
        for i in self.art_areay:
            for j in self.art_areax:
                if(j+defs.board_start-1>defs.board_len-1): 
                    return -1
                if defs.board_check[i][j+defs.board_start-1]==1 and not self._isSheilded:
                    return 1
                elif defs.board_check[i][j+defs.board_start-1]==1:
                    self._isSheilded=False
                    Bullet.clearArcs(j+defs.board_start-1,i)
                    return -1
                if defs.board_check[i][j+defs.board_start] == 2:
                    defs.board_check[i][j+defs.board_start]=0
                    defs.board_check[i][j+defs.board_start-1]=0
                    defs.board_check[i][j+defs.board_start+1]=0
                    game_stats.incrCoins()
                    return 2
                if defs.board_check[i][j+defs.board_start] == 5:
                    defs.board_check[i][j+defs.board_start]=0
                    defs.speed/=1.5
                    return 2

    def return_coins(self):
        return game_stats.coinsCollected


    def print_rider(self):
        for i in self.rider:
            print(i)
        for i in range(len(self.rider)):
            for j in range(len(self.rider[0])):
                val = ""
                for x in self.rider[i][j]:
                    if(type(x)!=int):
                        val+=x
                print(val,end="")
            # if i!=int(rows)-1 and j!=int(columns)-1:
            print(reset_color)
            # else:
            print("",end="")
        print(reset_color,end="",flush=True)
        print(self.art_areax)
        print(self.art_areay)
        for i in self.art_areay:
            for j in self.art_areax:
                print(reset_color,"\n",i,j+int(columns)*(defs.board_start))
# x = Rider()
# x.print_rider()