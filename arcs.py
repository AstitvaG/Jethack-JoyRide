from random import randint
import os
from clouds import board_len

reset_color="\x1B[0m"
rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)

col_yf='\x1B[38;2;255;255;0m'
col_of='\x1b[38;2;255;165;0m'
col_ob='\x1b[48;2;255;165;0m'

arc_v = [[col_yf, col_ob, '▐' , '', 1], [col_of, '', '▌' , '', -1]]
arc_h = [[col_of, '', '▂' , '', 1], [col_yf, col_ob, '▀' , '', -1]]
arc_r = [
            [['','',' ','',-1],[col_yf, col_ob, '▗' , '', 1],[col_of,'','▖','',-1]],
            [[col_of,'','▝','',-1],[col_yf, col_ob, '▚' , '', 1],[col_of,'','▖','',-1]],
            [[col_of,'','▝','',-1],[col_yf, col_ob, '▘' , '', 1],['','',' ','',-1]]
        ]
arc_l = [
            [[col_of,'','▗','',-1],[col_yf, col_ob, '▖' , '', 1],['','',' ','',-1]],
            [[col_of,'','▗','',-1],[col_yf, col_ob, '▞' , '', 1],[col_of,'','▘','',-1]],
            [['','',' ','',-1],[col_yf, col_ob, '▝' , '', 1],[col_of,'','▘','',-1]]
        ]

for j in range(rows//2):
    for i in arc_v:
        val=""
        for x in i:
            if(type(x) != int):
                val+=x
        print(val+reset_color,end="")
    print()
print()


for i in range(len(arc_h)):
    for j in range(rows):
        val=""
        for x in arc_h[i]:
            if(type(x) != int):
                val+=x
        print(val+reset_color,end="")
    print()
print()



for j in range(rows//2):
    if j>0 and j<rows//2-1: g=1
    elif j==0: g=0
    else: g=2
    val=""
    for x in arc_r[g]:
        for p in x:
            if(type(p) != int):
                val+=p
        val+=reset_color
    print(' '*j,end="")
    print(val)
print()

for j in range(rows//2-1,-1,-1):
    if j>0 and j<rows//2-1: g=1
    elif j==0: g=2
    else: g=0
    val=""
    for x in arc_l[g]:
        for p in x:
            if(type(p) != int):
                val+=p
        val+=reset_color
    print(' '*j,end="")
    print(val)
print()


def fill_in_art(board,freq,art):
    for p in range(board_len//freq):
        starty=randint(3,freq-3-len(art[0]))+p*freq
        startx=randint(3,int(rows)-3-len(art))
        i=0
        j=0
        for i in range(len(art)):
            for j in range(len(art[0])):
                if art[i][j]==1:
                    pass
                    # board[startx+i][starty+j]=(fn=37,end="\x1B[36m\x1B[46m")
                    # print(add_element(fn=37,end="\x1B[36m\x1B[46m"))