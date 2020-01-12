from random import randint
import os
# from main import add_element
block = "\u2588"
board_len = 10000




def add_element(temp_list=None,cont=-1,fn=-1,bn=-1,r1=0,g1=0,b1=0,bx=-1,r2=0,g2=0,b2=0,element=block,end=""):
    """
    fg in rgb: just put r1,g1,b1\n
    else : put value of fn\n
    bg in rgb: just put r2,g2,b2 as well as bx=1\n
    bg in rgb: to copy fg in rgb : bx=0
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
            

rows, columns = os.popen('stty size', 'r').read().split()
block = "\u2588"

large_cloud = [[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
               [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0]]

small_cloud = [[0,0,0,1,1,1,0,0],
               [0,0,1,1,1,1,1,0],
               [1,1,1,1,1,1,1,1]]

# def print_cloud(art):
#     for i in range(len(art)):
#         for j in range(len(art[0])):
#             if(art[i][j]==0):
#                 value = "\x1B[36m"
#             else:
#                 value = "\x1B[37m"
#             print(value+block,end="")
#         print(reset_color)

def fill_in_art(board,freq,art):
    for p in range(board_len//freq):
        starty=randint(3,freq-3-len(art[0]))+p*freq
        startx=randint(3,int(rows)-3-len(art))
        i=0
        j=0
        for i in range(len(art)):
            for j in range(len(art[0])):
                if art[i][j]==1:
                    board[startx+i][starty+j]=add_element(fn=37,end="\x1B[36m\x1B[46m")
                    # print(add_element(fn=37,end="\x1B[36m\x1B[46m"))
