import os, time, threading, _thread,math
from clouds import fill_in_clouds,small_cloud,large_cloud,add_element
from rider import Rider
from input import input_to, Get
from random import sample
from arcs import fill_in_art
from defs import rows,columns,fg,bg,reset_color,board_len
from coins import fill_in_coins
import defs,copy,bullet,powerup,enemy,magnet

start_time = time.time()


def print_board(board_start):
    board=defs.board
    print("",end="\033[0;0f")
    for i in range(int(rows)):
        for j in range(int(columns)):
            val=""
            if (i in main_rider.art_areay) and (j in main_rider.art_areax):
                ix=main_rider.art_areay.index(i)
                iy=main_rider.art_areax.index(j)
                if main_rider.rider[ix][iy][4] == 1:
                    for x in main_rider.rider[ix][iy]:
                        if(type(x)!=int):
                            val+=x
                else:
                    val = main_rider.rider[ix][iy][0]\
                            +defs.plain_board[i][j+board_start][1]\
                            +main_rider.rider[ix][iy][2]\
                            +main_rider.rider[ix][iy][3]
                val+=bg+fg
                print(val,end="")
            elif j+board_start-defs.enemyrelpos<defs.board_len-1 and\
            defs.board_check[i][j+board_start-defs.enemyrelpos] in [6,7,8]:
                b = enemy.Enemy.fill_in(defs.board_check[i][j+board_start-defs.enemyrelpos])
                print(b[0]+b[1]+b[2]+b[3],end="")
            elif defs.board_check[i][j+board_start] in range(10,19):
                b = magnet.Magnet.fill_in(defs.board_check[i][j+board_start])
                if b[4]==-1:
                    val = b[0]+defs.plain_board[i][j+board_start][1]+b[2]+b[3]
                else:
                    val=b[0]+b[1]+b[2]+b[3]
                print(val,end="")
            elif defs.board_check[i][j+board_start]==0:
                for x in defs.plain_board[i][j+board_start]:
                    val+=x
                print(val,end="")
            elif defs.board_check[i][j+board_start] in [9,30]:
                b = bullet.Bullet.fill_in(defs.board_check[i][j+board_start])
                print(b[0]+defs.plain_board[i][j+board_start][1]+b[2]+b[3],end="")
            elif defs.board_check[i][j+board_start]==5:
                b = powerup.Powerup.fill_in()
                print(b[0]+b[1]+b[2]+b[3],end="")
            else:
                for x in board[i][j+board_start]:
                    val+=x
                print(val,end="")
        if i!=int(rows)-1 and j!=int(columns)-1:
            print()
        else:
            print("",end="")
    print(reset_color,end="",flush=True)
    print("",end="\033[0;0f")
    
    print(reset_color,"Coins collected :",defs.coinsCollected,\
        "\tEnemies killed :",defs.enemiesKilled,\
        "\tBullets fired :",defs.bulletsFired,\
        "\tTime :",math.floor(time.time()-start_time),\
        "\tLives :",defs.livesleft,defs.dragonlivesleft,defs.speed)




def create_board():
    board = list()
    for i in range(int(rows)):
        temp_list = list()
        for _ in range(board_len):
            if(i==0):
                add_element(temp_list,fn=34)
            elif(i==1):
                add_element(temp_list,fn=34)
            elif(i==int(rows)-1):
                add_element(temp_list,fn=32)
            else:
                add_element(temp_list,cont=1)
        board.append(temp_list)
    fill_in_clouds(board,30,small_cloud)
    fill_in_clouds(board,100,large_cloud)
    defs.plain_board=copy.deepcopy(board)
    for i in range(2,board_len//(2*int(rows)//3+1)):
        val=sample(range(1,5),2)
        try:
            fill_in_art(board,val[0],2*int(rows)//3+1,i)
        except:pass
        try:
            fill_in_art(board,val[1],2*int(rows)//3+1,i)
        except:pass
    fill_in_coins(board,100)
    powerup.Powerup(defs.board_len//5)
    enemy.Enemy(40)
    magnet.Magnet(200,10)
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
    board_start = time.time()
    while defs.board_start+int(columns)<=board_len and\
    defs.dragonlivesleft>=0 and defs.livesleft>=0:
        print_board(defs.board_start)
        time.sleep(defs.speed)
        defs.board_start+=1
        defs.enemyrelpos-=2
        main_rider.move('a',True)
        main_rider.move('s',val=defs.down)
        defs.down+=1
        if stop():
            print("\033[2J",end="")
            _thread.interrupt_main()
        if time.time()-board_start>40:
            defs.speed=round(defs.speed*0.8,4)
            board_start=time.time()

if __name__=="__main__":
    main_rider = Rider()
    defs.board_check = create_check()
    defs.board = create_board()
    for i in range(int(rows)):
        defs.board[i][board_len-1]=add_element(fn=33,end=fg+bg)
        defs.board[i][board_len-10]=add_element(fn=33,end=fg+bg)
        defs.board[i][board_len-2]=add_element(fn=33,end=fg+bg)
        defs.board[i][board_len-3]=add_element(fn=33,end=fg+bg)
    stop_threads = False
    thread1 = threading.Thread(target=increase_strt, daemon=True, args =(lambda : stop_threads, ))
    thread1.start()
    while defs.dragonlivesleft>=0 and defs.livesleft>=0:
        getch = Get()
        chbuff = input_to(getch)
        if chbuff:
            if chbuff =='q':
                defs.livesleft = -2
                time.sleep(0.2)
                print("\033[2J",end="")
                exit(0)
            elif chbuff in ['w','a','s','d']:
                main_rider.move(chbuff)
                if chbuff=='w': defs.down=1
                else: defs.down=1
            elif chbuff == 'j':
                # print(main_rider.xpos_left,main_rider.ypos_top)
                bullet.Bullet(main_rider.xpos_left+defs.board_start+len(main_rider.rider[0]),\
                    main_rider.ypos_top,2*int(defs.columns))
            elif chbuff == ' ':
                main_rider.sheild() 
        elif not main_rider._isSheilded:
            main_rider.change_rider(0)
        main_rider.check_pos()
