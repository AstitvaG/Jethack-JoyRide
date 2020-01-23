from random import randint
import os,defs
from defs import block,rows

def add_element(temp_list=None,cont=-1,fn=-1,bn=-1,r1=0,g1=0,b1=0,bx=-1,r2=0,g2=0,b2=0,element=block,end=""):
    """
    fg in rgb: just put r1,g1,b1\n
    else : put value of fn\n
    bg in rgb: just put r2,g2,b2 as well as bx=1\n
    bg in rgb: to copy fg in rgb : bx=0\n
    else : just put bn
    """
    f=False
    if(temp_list==None):
        f=True
        temp_list = list()
    if cont == 1:
        temp_list.append(["","",element,""])
        if f==True:
            return temp_list[0]
        return
    if fn != -1:
        if (bn==-1 and bx==-1) or bn!=-1:
            if bn==-1: bn=fn+10
            temp_list.append(["\x1B["+str(fn)+"m",
                              "\x1B["+str(bn)+"m",
                              element,
                              end])
        else:
            temp_list.append(["\x1B["+str(fn)+"m",
                              "\x1b[48;2;"+str(r2)+";"+str(g2)+";"+str(b2)+"m",
                              element,
                              end])

    else:
        if bx>0:
            temp_list.append(["\x1b[38;2;"+str(r1)+";"+str(g1)+";"+str(b1)+"m",
                              "\x1b[48;2;"+str(r2)+";"+str(g2)+";"+str(b2)+"m",
                              element,
                              end])
        elif bx==0:
            temp_list.append(["\x1b[38;2;"+str(r1)+";"+str(g1)+";"+str(b1)+"m",
                              "\x1b[48;2;"+str(r1)+";"+str(g1)+";"+str(b1)+"m",
                              element,
                              end])
        else:
            temp_list.append(["\x1b[38;2;"+str(r1)+";"+str(g1)+";"+str(b1)+"m",
                              "\x1B["+str(bn)+"m",
                              element,
                              end])
    if(f==True):
        return temp_list[0]
            

large_cloud = [[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
               [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0]]

small_cloud = [[0,0,0,1,1,1,0,0],
               [0,0,1,1,1,1,1,0],
               [1,1,1,1,1,1,1,1]]

class Clouds:
    def fill_in_clouds(self,board,freq,art):
        for p in range(defs.board_len//freq):
            startx=randint(3,freq-3-len(art[0]))+p*freq
            starty=randint(3,int(rows)-3-len(art))
            i=0
            j=0
            for i in range(len(art)):
                for j in range(len(art[0])):
                    if art[i][j]==1:
                        board[starty+i][startx+j]=add_element(fn=37,end=defs.bg+defs.fg)

    def __init__(self,freq,board):
        self.fill_in_clouds(board,int(0.4*freq),small_cloud)
        self.fill_in_clouds(board,freq,large_cloud)
