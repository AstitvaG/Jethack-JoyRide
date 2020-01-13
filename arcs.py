from random import randint
import os
reset_color="\x1B[0m"
# from clouds import *

col_yf='\x1B[38;2;255;255;0m'
col_of='\x1b[38;2;255;165;0m'
col_ob='\x1b[48;2;255;165;0m'

arc_h = [[col_of, '', '▂' , '', 1], [col_yf, col_ob, '▀' , '', -1]]
arc_v = [[col_yf, col_ob, '▐' , '', 1], [col_of, '', '▌' , '', -1]]
arc_r = [[col_yf, col_ob, '▗' , '', 1], [col_yf, col_ob, '▚' , '', 1], [col_yf, col_ob, '▘' , '', 1]]
arc_l = [[col_yf, col_ob, '▖' , '', 1], [col_yf, col_ob, '▞' , '', 1], [col_yf, col_ob, '▝' , '', 1]]

# def fill_in_art1(board,freq,art):
#     for p in range(board_len//freq):
#         starty=randint(3,freq-3-len(art[0]))+p*freq
#         startx=randint(3,int(rows)-3-len(art))
#         i=0
#         j=0
#         for i in range(len(art)):
#             for j in range(len(art[0])):
#                 if art[i][j]==1:
#                     board[startx+i][starty+j]=add_element(fn=37,end="\x1B[36m\x1B[46m")
#                     print(add_element(fn=37,end="\x1B[36m\x1B[46m"))
for j in range(10):
    for i in arc_v:
        val=""
        for x in i:
            if(type(x) != int):
                val+=x
        print(val+reset_color,end="")
    print()
print()
for i in range(len(arc_h)):
    for j in range(10):
        val=""
        for x in arc_h[i]:
            if(type(x) != int):
                val+=x
        print(val+reset_color,end="")
    print()
print()

for j in range(10):
    if j>0 and j<9: g=1
    elif j==0: g=0
    else: g=2
    val=""
    for x in arc_r[g]:
        if(type(x) != int):
            val+=x
    print(' '*j,end="")
    print(val+reset_color)
print()
for j in range(9,-1,-1):
    if j>0 and j<9:
        g=1
    elif j==0:
        g=2
    else:
        g=0
        # print(' '*j,end='')
    if j>0 and j<=9:
        print(' '*(j-1)+col_of+'▗',end="")
    val=""
    for x in arc_l[g]:
        if(type(x) != int):
            val+=x
    # print(' '*j,end="")
    if j>=0 and j<9:
        val+=reset_color+col_of+'▘'
    print(val+reset_color)
# val=""
# for x in arc_r[2]:
#     if(type(x) != int):
#         val+=x
# print(" "+val+reset_color)

# for j in range(10):
#     for i in arc_h:
#         print(i+reset_color)