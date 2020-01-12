import os, time, threading
from clouds import fill_in_art,small_cloud,large_cloud,add_element,board_len
from rider import *

rows, columns = os.popen('stty size', 'r').read().split()
reset_color="\x1B[0m"
block = "\u2588"
board = list()


def print_board1(board,board_start):
    print("",end="\033[0;0f")
    for i in range(int(rows)):
        for j in range(int(columns)):
            val = ""
            for x in board[i][j+board_start]:
                val+=x
            print(val,end="")
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
        if i!=int(rows)-1 and j!=int(columns)-1:
            print()
        else:
            print("",end="")
    print(reset_color,end="",flush=True)


def create_board():
    board = list()
    for i in range(int(rows)):
        temp_list = list()
        for j in range(board_len):
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



def create_board1():
    board = list()
    for i in range(int(rows)):
        temp_list = list()
        for j in range(board_len):
            if(i==0):
                add_element(temp_list,fn=34)
            elif(i==1):
                add_element(temp_list,fn=36)
            elif(i==int(rows)-1):
                add_element(temp_list,fn=32)
            else:
                add_element(temp_list,cont=1)
        board.append(temp_list)
    fill_in_art(board,30,small_cloud)
    fill_in_art(board,100,large_cloud)
    return board



def increase_strt(board_start=0):
    # print_board1(board,board_start)
    while(board_start+int(columns)<=board_len):
        print_board1(board,board_start)
        time.sleep(0.00001)
        board_start+=1

            
if __name__=="__main__":
    # print_rider(rider)
    # board = create_board()
    # for i in range(int(rows)):
    #     board[i][2999]="\x1B[33m"+block+"\x1B[36m"
    #     board[i][2999]=add_element(fn=33)

    
    # main_rider = Rider()
    # main_rider.print_rider()
    board = create_board1()
    for i in range(int(rows)):
        board[i][board_len-1]=add_element(fn=33,end="\x1B[36m")[0]
        board[i][board_len-10]=add_element(fn=33,end="\x1B[36m")[0]
        board[i][board_len-2]=add_element(fn=33,end="\x1B[36m")[0]
    thread = threading.Thread(target=increase_strt)
    thread.start()

    # print_board(board)
