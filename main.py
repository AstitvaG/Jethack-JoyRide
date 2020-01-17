import os, time, threading
from clouds import fill_in_clouds,small_cloud,large_cloud,add_element
from rider import Rider
from input import input_to, Get
from random import sample
from arcs import fill_in_art
from defs import rows,columns,fg,bg,reset_color,board_len
from coins import fill_in_coins
import defs


def print_board(board,board_start):
    print("",end="\033[0;0f")
    for i in range(int(rows)):
        for j in range(int(columns)):
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
        if i!=int(rows)-1 and j!=int(columns)-1:
            print()
        else:
            print("",end="")
    print(reset_color,end="",flush=True)



def create_board():
    board = list()
    for i in range(int(rows)):
        temp_list = list()
        for _ in range(board_len):
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
    for i in range(2,board_len//100):
        val=sample(range(1,5),2)
        fill_in_art(board,val[0],i,int(columns)//3)
        fill_in_art(board,val[1],i,int(columns)//3)
    fill_in_coins(board,100)
    return board

def create_check():
    defs.board_check = list()
    for _ in range(int(rows)):
        temp_list = list()
        for _ in range(board_len):
            temp_list.append(0)
        defs.board_check.append(temp_list)
    return defs.board_check



def increase_strt(stop):
    while(defs.board_start+int(columns)<=board_len):
        print_board(board,defs.board_start)
        time.sleep(0.1)
        defs.board_start+=1
        main_rider.move('s')
        main_rider.move('a')
        if main_rider.check_pos() ==2:
            print_board(board,defs.board_start)
            break
        if stop():
            break

if __name__=="__main__":
    main_rider = Rider()
    defs.board_check = create_check()
    board = create_board()
    for i in range(int(rows)):
        board[i][board_len-1]=add_element(fn=33,end=fg+bg)
        board[i][board_len-10]=add_element(fn=33,end=fg+bg)
        board[i][board_len-2]=add_element(fn=33,end=fg+bg)
        board[i][board_len-3]=add_element(fn=33,end=fg+bg)
    stop_threads = False
    thread1 = threading.Thread(target=increase_strt, daemon=True, args =(lambda : stop_threads, ))
    thread1.start()
    # thread2 = threading.Thread(target=gravity, daemon=True, args =(lambda : stop_threads, ))
    # thread2.start()
    while True:
        getch = Get()
        chbuff = input_to(getch)
        if chbuff:
            if chbuff =='q':
                stop_threads = True
                thread1.join(0)
                # thread2.join(0)
                print("\033[2J",end="")
                exit(0)
            elif chbuff in ['w','a','s','d']:
                main_rider.move(chbuff)
        if main_rider.check_pos() ==2:
            stop_threads = True
            thread1.join(0)
            print("\033[2J",end="")
            print_board(board,defs.board_start)
            break
