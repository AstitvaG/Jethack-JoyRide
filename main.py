import os, time, threading
from clouds import fill_in_clouds,small_cloud,large_cloud,add_element,board_len
from rider import *
from input import input_to, Get
from random import randint
from arcs import fill_in_art


rows, columns = os.popen('stty size', 'r').read().split()
reset_color="\x1B[0m"
block = "\u2588"
board = list()
main_rider = Rider()


def print_board1(board,board_start):
    print("",end="\033[0;0f")
    for i in range(int(rows)):
        for j in range(int(columns)):
            # print(i,j+board_start,end="\033[0;0f")
            val=""
            if (i not in main_rider.art_areay) or (j not in main_rider.art_areax):
                for x in board[i][j+board_start]:
                    val+=x
                print(val,end="")
            else:
                ix=main_rider.art_areay.index(i)
                iy=main_rider.art_areax.index(j)
                if main_rider.rider[ix][iy][4] == 1:
                    for x in main_rider.rider[ix][iy]:
                        if(type(x)!=int):
                            val+=x
                else:
                    val = main_rider.rider[ix][iy][0]\
                            +board[i][j+board_start][1]\
                            +main_rider.rider[ix][iy][2]\
                            +main_rider.rider[ix][iy][3]
                val+=bg+fg
                print(val,end="")
                # print("\x1B[33m\x1B[43m"+block+"\x1B[36m\x1B[46m",end="")

            # print(reset_color)
        if i!=int(rows)-1 and j!=int(columns)-1:
            print()
        else:
            print("",end="")
    print(reset_color,end="",flush=True)



def print_board(board,board_start):
    for i in range(int(rows)):
        for j in range(int(columns)):
            if (i not in main_rider.art_areay) or (j not in main_rider.art_areax):
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
                #blue
                temp_list.append("\x1B[34m\x1B[44m"+block)
            elif(i==1):
                #cyan
                temp_list.append("\x1B[36m\x1B[46m"+block)
            elif(i==int(rows)-1):
                #green
                temp_list.append("\x1B[32m\x1B[42m"+block)
            else:
                temp_list.append(block)
        board.append(temp_list)
    fill_in_clouds(board,30,small_cloud)
    fill_in_clouds(board,100,large_cloud)
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
    fill_in_clouds(board,30,small_cloud)
    fill_in_clouds(board,100,large_cloud)
    for i in range(board_len//100):
        val=randint(1,4)
        fill_in_art(board,val,i,int(columns)//3)

    return board



def increase_strt(stop,board_start=0):
    # print_board1(board,board_start)
    while(board_start+int(columns)<=board_len):
        print_board1(board,board_start)
        time.sleep(0.1)
        board_start+=1
        if stop():
            break
        

def gravity(stop):
    # print_board1(board,board_start)
    while True:
        time.sleep(0.1)
        main_rider.move('s')
        main_rider.move('a')
        if stop():
            break
            
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
        board[i][board_len-1]=add_element(fn=33,end=fg+bg)
        board[i][board_len-10]=add_element(fn=33,end=fg+bg)
        board[i][board_len-2]=add_element(fn=33,end=fg+bg)
        board[i][board_len-3]=add_element(fn=33,end=fg+bg)
    stop_threads = False
    thread1 = threading.Thread(target=increase_strt, daemon=True, args =(lambda : stop_threads, ))
    thread1.start()
    thread2 = threading.Thread(target=gravity, daemon=True, args =(lambda : stop_threads, ))
    thread2.start()
    while True:
        getch = Get()
        chbuff = input_to(getch)
        if chbuff:
            if chbuff =='q':
                stop_threads = True
                thread1.join(0)
                thread2.join(0)
                print("\033[2J",end="")
                exit(0)
            elif chbuff in ['w','a','s','d']:
                # os.system("clear")
                # exit(0)
                main_rider.move(chbuff)

        
    # print_board(board)
