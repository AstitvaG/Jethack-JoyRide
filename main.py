import os, time, threading
from clouds import fill_in_art,small_cloud,large_cloud
from rider import *

rows, columns = os.popen('stty size', 'r').read().split()
reset_color="\x1B[0m"
block = "\u2588"
board = list()



# def print_rider(art):
#     for i in range(len(art)):
#         for j in range(len(art[i])): 
#             print(art[i][j],end="")
#         print(reset_color)

def print_board1(board,board_start):
    for i in range(int(rows)):
        for j in range(int(columns)):
            rx = Rider()
            if (i not in rx.art_areay) or (j not in rx.art_areax):
                print(board[i][j+board_start],end="")
            else:
                print("\033[1C",end="")

            # if i  not in Rider.art_areay and j not in Rider.art_areax:
            # print(board[i][j+board_start],end="")
        if i!=int(rows)-1 and j!=int(columns)-1:
            print()
        else:
            print("",end="")
    print(reset_color,end="",flush=True)



def print_board(board,board_start):
    for i in range(int(rows)):
        for j in range(int(columns)):
            rx = Rider()
            if (i not in rx.art_areay) or (j not in rx.art_areax):
                print(board[i][j+board_start],end="")
            else:
                print("\033[1C",end="")

            # if i  not in Rider.art_areay and j not in Rider.art_areax:
            # print(board[i][j+board_start],end="")
        if i!=int(rows)-1 and j!=int(columns)-1:
            print()
        else:
            print("",end="")
    print(reset_color,end="",flush=True)

def create_board():
    board = list()
    for i in range(int(rows)):
        temp_list = list()
        for j in range(3000):
            if(i==0):
                temp_list.append("\x1B[34m\x1B[44m"+block)
            elif(i==1):
                temp_list.append("\x1B[36m\x1B[46m"+block)
            elif(i==int(rows)-1):
                temp_list.append("\x1B[32m\x1B[42m"+block)
            else:
                temp_list.append(block)
        board.append(temp_list)
    fill_in_art(board,30,small_cloud)
    fill_in_art(board,100,large_cloud)
    return board

def add_element(temp_list,fn=-1,bn=-1,fx=-1,r1=0,g1=0,b1=0,bx=-1,r2=0,g2=0,b2=0,element=block):
    if fn != -1:
        if bn==-1:
            bn=fn+10
        temp_list.append(["\x1B["+fn+"m","\x1B["+bn+"m",block])
    else:
        temp_list.append([""])
            

def create_board1():
    board = list()
    for i in range(int(rows)):
        temp_list = list()
        for j in range(3000):
            if(i==0):
                add_element(temp_list,fn=34)
                # temp_list.append("\x1B[34m\x1B[44m"+block)
            elif(i==1):
                add_element(temp_list,fn=36)
                # temp_list.append("\x1B[36m\x1B[46m"+block)
            elif(i==int(rows)-1):
                add_element(temp_list,fn=32)
                # temp_list.append("\x1B[32m\x1B[42m"+block)
            else:
                temp_list.append(block)
        board.append(temp_list)
    fill_in_art(board,30,small_cloud)
    fill_in_art(board,100,large_cloud)
    return board


# def print_rider(xstart=(int(columns)*10)//100,ystart=int(rows/2)):






def increase_strt(board_start=0):
    while(board_start+int(columns)<=len(board[0])):
        print("\033[0;0f",end="")
        print_board(board,board_start)
        time.sleep(0.01)
        board_start+=1

            
if __name__=="__main__":
    # print_rider(rider)
    board = create_board()
    for i in range(int(rows)):
        board[i][2999]="\x1B[33m"+block+"\x1B[36m"

    # print("\033[s",end="")
    
    main_rider = Rider()
    main_rider.print_rider()
    # time.sleep(10)
    thread = threading.Thread(target=increase_strt)
    thread.start()

    # print_board(board)
