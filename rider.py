import os
from clouds import add_element
from defs import reset_color,rows,columns
import defs
from stats import Stats

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
    # rider = [[bg+" ",gc("\u2585",224,172,172,f=0,e=0)],
    #           [gc("\u2589"),gc("\u2588",b=139,e=0)],
    #           [gc("\u2598",252,186,3),gc("\u259B",e=0)]]
    # rider = list()
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
        if val==0:
            self.rider=self.rider_normal

    def __init__(self):
        # self.gen_rider()
        self._xpos_left = 4
        self._ypos_top = int(rows)//2
        self.art_areax=range(self._xpos_left,self._xpos_left+len(self.rider[0]))
        self.art_areay=range(self._ypos_top,self._ypos_top+len(self.rider))
        # self.print_rider()

    def move(self,chbuff):
        if chbuff == 'w':
            self._ypos_top -= 4
            if self._ypos_top<-1:
                self._ypos_top=-1
            self.change_rider(1)
        elif chbuff == 's':
            self._ypos_top += 2
            if self._ypos_top>int(rows)-4:
                self._ypos_top=int(rows)-4
        elif chbuff == 'a':
            self._xpos_left -= 1
            if self._xpos_left<0:
                self._xpos_left=0
        elif chbuff == 'd':
            self._xpos_left += 3
            if self._xpos_left>int(columns)-2:
                self._xpos_left=int(columns)-2
            self.change_rider(1)
        self.art_areax=range(self._xpos_left,self._xpos_left++len(self.rider[0]))
        self.art_areay=range(self._ypos_top,self._ypos_top++len(self.rider))
       
    def check_pos(self):
        for i in self.art_areay:
            for j in self.art_areax:
                if(j+defs.board_start-1>defs.board_len-1): return -1
                if defs.board_check[i][j+defs.board_start-1]==1:
                    return 1
                if defs.board_check[i][j+defs.board_start-1] == 2:
                    defs.board_check[i][j+defs.board_start-1]=0
                    defs.board_check[i][j+defs.board_start-2]=0
                    defs.board_check[i][j+defs.board_start]=0
                    game_stats.incrCoins()
                    return 2



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