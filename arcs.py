from random import randint
import os
from rider import Rider
from defs import rows,fg,bg,reset_color
import defs,random

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


class Arcs:
    def fill_in_art(self,board,val,freq,iter):
        if val==1:
            starty=randint(1,rows//3-1) #changing
            startx=randint(1,freq-1)+iter*freq #const
            for j in range(rows//3):
                i=0
                for idx in arc_v:
                    if idx[4] == -1:
                        val = [idx[0],board[starty+j][startx+i][1],idx[2],bg+fg]
                    else:
                        val = [idx[0],idx[1],idx[2],bg+fg]
                    
                    board[starty+j][startx+i]=val
                    defs.board_check[starty+j][startx+i]=1
                    i+=1
        elif val==2:
            starty=randint(1,rows-3) #const
            startx=randint(1,freq-1)+iter*freq #const
            for j in range(2*rows//3):
                i=0
                for idx in arc_h:
                    if idx[4] == -1:
                        val = [idx[0],board[starty+i][startx+j][1],idx[2],bg+fg]
                    else:
                        val = [idx[0],idx[1],idx[2],bg+fg]
                    board[starty+i][startx+j]=val
                    defs.board_check[starty+i][startx+j]=1
                    i+=1
        elif val==3:
            starty=randint(1,rows//3-1) #changing
            startx=randint(1,freq-1)+iter*freq #const
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
                    defs.board_check[starty+j][startx+i+j]=1
                    i+=1
        else:
            starty=randint(1,rows//3-1) #changing
            startx=randint(1,freq-1)+iter*freq #const
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
                    defs.board_check[starty+j][startx+i-j]=1
                    i+=1

    def __init__(self,freq,board):
        for i in range(2,defs.board_len//freq):
            val=random.sample(range(1,5),2)
            try:
                self.fill_in_art(board,val[0],freq+1,i)
            except:pass
            try:
                self.fill_in_art(board,val[1],freq+1,i)
            except:pass