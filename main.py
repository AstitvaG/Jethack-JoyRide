import os, time, threading
from clouds import fill_in_clouds,small_cloud,large_cloud,add_element
from rider import Rider
from input import input_to, Get
from random import randint
from arcs import fill_in_art
from defs import rows,columns,fg,bg,reset_color,board_len


def print_board1(board,board_start):
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



def create_board1():
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
    for i in range(board_len//100):
        val=randint(1,4)
        fill_in_art(board,val,i,int(columns)//3)

    return board



def increase_strt(stop,board_start=0):
    while(board_start+int(columns)<=board_len):
        print_board1(board,board_start)
        time.sleep(0.1)
        board_start+=1
        if stop():
            break
        

def gravity(stop):
    while True:
        time.sleep(0.1)
        main_rider.move('s')
        main_rider.move('a')
        if stop():
            break
            
if __name__=="__main__":
    main_rider = Rider()
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
                main_rider.move(chbuff)
