from random import randint
import os
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
    for p in range(3000//freq):
        starty=randint(3,freq-3-len(art[0]))+p*freq
        startx=randint(3,int(rows)-3-len(art))
        print("",end="",flush=True)
        i=0
        j=0
        for i in range(len(art)):
            for j in range(len(art[0])):
                if art[i][j]==1:
                    board[startx+i][starty+j]="\x1B[37m"+block+"\x1B[36m"
