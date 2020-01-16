from random import randint
import os
from clouds import board_len
from rider import Rider

reset_color="\x1B[0m"
rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)

col_yf='\x1B[38;2;255;255;0m'
col_of='\x1b[38;2;255;165;0m'
col_ob='\x1b[48;2;255;165;0m'

arc_v = [[col_yf, col_ob, '▐' , '', 1], [col_of, '', '▌' , '', -1]]
arc_h = [[col_of, '', '▂' , '', -1], [col_yf, col_ob, '▀' , '', 1]]
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

bg = "\x1B[46m"
fg = "\x1B[36m"

def fill_in_art(board,val,freq,len):
    if val==1:
        starty=randint(1,rows//3-1) #changing
        startx=randint(len*freq,len*(freq+1)-1) #const
        for j in range(rows//3):
            i=0
            for idx in arc_v:
                if idx[4] == -1:
                    val = [idx[0],board[starty+j][startx+i][1],idx[2],bg+fg]
                else:
                    val = [idx[0],idx[1],idx[2],bg+fg]
                
                board[starty+j][startx+i]=val
                i+=1
    elif val==2:
        starty=randint(1,rows-3) #const
        startx=randint(len*freq,len*(freq+1)-rows-1) #changing
        for j in range(2*rows//3):
            i=0
            for idx in arc_h:
                # try:
                if idx[4] == -1:
                    val = [idx[0],board[starty+i][startx+j][1],idx[2],bg+fg]
                else:
                    val = [idx[0],idx[1],idx[2],bg+fg]
                board[starty+i][startx+j]=val
                i+=1
    elif val==3:
        starty=randint(1,rows//3-1) #changing
        startx=randint(len*freq,len*(freq+1)-1) #const
        for j in range(rows//3):
            if j == 0: p = arc_r[0]
            elif j == rows//3-1: p = arc_r[2]
            else : p = arc_r[1]
            i=0
            for idx in p:
                if idx[4] == -1:
                    val = [idx[0],board[starty+j][startx+i+j][1],idx[2],bg+fg]
                else:
                    val = [idx[0],idx[1],idx[2],bg+fg]
                
                board[starty+j][startx+i+j]=val
                i+=1
    else:
        starty=randint(1,rows//3-1) #changing
        startx=randint(len*freq,len*(freq+1)-1) #const
        for j in range(rows//3-1,-1,-1):
            if j == 0: p = arc_l[0]
            elif j == rows//3-1: p = arc_l[2]
            else : p = arc_l[1]
            i=0
            for idx in p:
                if idx[4] == -1:
                    val = [idx[0],board[starty+j][startx+i-j][1],idx[2],bg+fg]
                else:
                    val = [idx[0],idx[1],idx[2],bg+fg]
                
                board[starty+j][startx+i-j]=val
                i+=1

def print_arcs():
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
