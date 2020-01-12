import os
rows, columns = os.popen('stty size', 'r').read().split()
block = "\u2588"

rows, columns = os.popen('stty size', 'r').read().split()
reset_color="\x1B[0m"
block = "\u2588"
board = list()
bg = "\x1B[46m"

def gc(c="\u2588",r=0,g=0,b=0,f=1,e=1,c1="",r1=0,g1=0,b1=0):
    ret_str = "\x1b[38;2;"+str(r)+";"+str(g)+";"+str(b)+"m"+str(c)
    if f==0:
        ret_str = "\x1b[38;2;"+str(r)+";"+str(g)+";"+str(b)+"m"+str(c1)
        ret_str += "\x1b[48;2;"+str(r1)+";"+str(g1)+";"+str(b1)+"m"+str(c)
    if e==1:
        ret_str+=reset_color
    return ret_str

class Rider:
    rider = [[bg+" ",gc("\u2585",224,172,172,f=0,e=0)],
              [gc("\u2589"),gc("\u2588",b=139,e=0)],
              [gc("\u2598",252,186,3),gc("\u259B",e=0)]]
    def __init__(self):
        self._xpos_left = 4
        self._ypos_top = int(rows)//2
        self.art_areax=range(self._xpos_left-1,self._xpos_left+len(self.rider[0])-1)
        self.art_areay=range(self._ypos_top-1,self._ypos_top+len(self.rider)-1)
    def print_rider(self):
        print("\033[" + str(self._ypos_top) + ";" + str(self._xpos_left) + "f",end="")
        for i in range(len(self.rider)):
            for j in range(len(self.rider[0])):
                print(bg+self.rider[i][j],end="")
            print("\033[2D",end="")
            print("\033[1B",end="")
        print("\033[0;0f",end="")