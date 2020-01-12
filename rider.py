import os
from clouds import add_element
rows, columns = os.popen('stty size', 'r').read().split()
block = "\u2588"

rows, columns = os.popen('stty size', 'r').read().split()
reset_color="\x1B[0m"
block = "\u2588"
board = list()
bg = "\x1B[46m"
fg = "\x1B[36m"

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
    rider = list()
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
    def __init__(self):
        self.gen_rider()
        self._xpos_left = 4
        self._ypos_top = int(rows)//2
        self.art_areax=range(self._xpos_left,self._xpos_left+2)
        self.art_areay=range(self._ypos_top,self._ypos_top+3)
    def move(self,chbuff):
        if chbuff == 'w':
            self._ypos_top -= 6
            if self._ypos_top<1:
                self._ypos_top=1
        if chbuff == 's':
            self._ypos_top += 2
            if self._ypos_top>int(rows)-4:
                self._ypos_top=int(rows)-4
        if chbuff == 'a':
            self._xpos_left -= 1
            if self._xpos_left<0:
                self._xpos_left=0
        if chbuff == 'd':
            self._xpos_left += 1
            if self._xpos_left>int(columns)-2:
                self._xpos_left=int(columns)-2
        self.art_areax=range(self._xpos_left,self._xpos_left+2)
        self.art_areay=range(self._ypos_top,self._ypos_top+3)
    
            

    # def print_rider(self):
        # for i in range(len(self.rider)):
        #     for j in range(len(self.rider[0])):
        #         val = ""
        #         for x in self.rider[i][j]:
        #             if(type(x)!=int):
        #                 val+=x
        #         print(val,end="")
        #     # if i!=int(rows)-1 and j!=int(columns)-1:
        #     print(reset_color)
            # else:
                # print("",end="")
        # print(reset_color,end="",flush=True)

x=Rider()