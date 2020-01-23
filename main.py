import os, time, threading, _thread,math
from input import input_to, Get
import defs,copy,bullet,powerup,enemy,magnet,stats,coins,inp,rider,clouds,arcs
from subprocess import call

def print_board():
    '''
    Print the whole completely again and again 
    '''

    k=defs.board_start
    print("",end="\033[0;0f")
    for i in range(int(defs.rows)):
        for j in range(int(defs.columns)):
            val=""
            
            # Stats
            if (i in stats.Stats.rangey) and (j in stats.Stats.rangex):
                stats.Stats.print_f(i,j)
            
            # Rider
            elif (i in defs.main_rider.art_areay) and (j in defs.main_rider.art_areax):
                ix=defs.main_rider.art_areay.index(i)
                iy=defs.main_rider.art_areax.index(j)
                if defs.main_rider.rider[ix][iy][4] == 1:
                    for x in defs.main_rider.rider[ix][iy]:
                        if(type(x)!=int):
                            val+=x
                else:
                    val = defs.main_rider.rider[ix][iy][0]\
                            +defs.plain_board[i][j+defs.board_start][1]\
                            +defs.main_rider.rider[ix][iy][2]\
                            +defs.main_rider.rider[ix][iy][3]
                val+=defs.bg+defs.fg
                print(val,end="")
            
            #Enemy
            elif enemy.Enemy.check_x(i,j+k):
                enemy.Enemy.print_f(i,j+k)
            
            # Magnets
            elif magnet.Magnet.check_x(i,j+k):
                magnet.Magnet.print_f(i,j+k)
            
            # Already empty or that made empty later
            elif defs.board_check[i][j+k]==0:
                for x in defs.plain_board[i][j+k]:
                    val+=x
                print(val,end="")
            
            # Bullets
            elif bullet.Bullet.check_x(i,j+k):
                bullet.Bullet.print_f(i,j+k)
            
            # Powerups
            elif powerup.Powerup.check_x(i,j+k):
                powerup.Powerup.print_f(i,j)
            
            # Prefilled values: Clouds, Arcs etc
            else:
                for x in defs.board[i][j+defs.board_start]:
                    val+=x
                print(val,end="")
    print(defs.reset_color,end="",flush=True)
    
    # Check if scoreboard is printed once or not 
    if not defs.oncePrinted:
        defs.oncePrinted=True
    print_sbValues()

def print_sbValues():
    '''
    Prints values inside the scoreboard
    '''
    pos1x = int(defs.columns)//2-(3*stats.valx)//8
    pos1y = 4
    print("",end="\033["+str(pos1y)+";"+str(pos1x)+"f"+stats.wb+stats.bf)
    print("Lives:\x1B[31m",'❤ '*defs.livesleft,end='       ')
    pos1y+=2
    print("",end="\033["+str(pos1y)+";"+str(pos1x)+"f"+stats.wb+stats.bf)
    print("Time left:",defs.total_time-int(time.time()-defs.start_time),end='  ')
    pos1x = int(defs.columns)//2+(stats.valx)//8
    pos1y = 4
    print("",end="\033["+str(pos1y)+";"+str(pos1x)+"f"+stats.wb+stats.bf)
    print(coins.col_gf+"⬤"+stats.bf+" x"+str(defs.coinsCollected)+"  E x"+str(defs.enemiesKilled),end='')
    pos1y+=2
    print("",end="\033["+str(pos1y)+";"+str(pos1x)+"f"+stats.wb+stats.bf)
    print("Score:",defs.coinsCollected+2*defs.enemiesKilled,end='')
    print("",end=defs.reset_color+"\033[0;0f",flush=True)

def create_board():
    '''
    Creates board and fills in Obstacles and Scenery
    '''
    board = list()
    for i in range(int(defs.rows)):
        temp_list = list()
        for _ in range(defs.board_len):
            if i==0 or i==0:
                clouds.add_element(temp_list,fn=34)
            elif i==int(defs.rows)-1 :
                clouds.add_element(temp_list,fn=32)
            else:
                clouds.add_element(temp_list,cont=1)
        board.append(temp_list)
    defs.board_len-=int(defs.columns)
    #
    clouds.Clouds(100,board)
    defs.plain_board=copy.deepcopy(board)
    arcs.Arcs((2*int(defs.rows)//3+1),board)
    coins.Coins(100,board)
    powerup.Powerup(defs.board_len//5)
    enemy.Enemy(40)
    magnet.Magnet(200,10)
    #
    defs.board_len+=int(defs.columns)
    return board

def create_check():
    '''
    Creates check board initialised to zero
    '''
    defs.board_check = list()
    for _ in range(int(defs.rows)):
        temp_list = list()
        for _ in range(defs.board_len):
            temp_list.append(0)
        defs.board_check.append(temp_list)
    return defs.board_check

def increase_strt():
    '''
    Thread function responsible for iterating through the board
    '''
    defs.start_time=time.time()
    board_time = time.time()
    grav_time = time.time()
    while defs.board_start+int(defs.columns)<=defs.board_len and\
    defs.dragonlivesleft>=0 and defs.livesleft>=0:
        print_board()
        time.sleep(defs.speed)
        defs.board_start+=1
        defs.enemyrelpos-=2
        defs.main_rider.move('a',True)
        defs.main_rider.move('s',val=defs.down)
        if time.time()-grav_time >defs.def_speed:
            defs.down+=1
            grav_time=time.time()
        if time.time()-board_time>40:
            defs.speed=round(defs.speed*0.8,4)
            board_time=time.time()
    if defs.livesleft>=0:
        defs.isbossfight=True

def input_handler():
    '''
    Handles user input and moves the character accordingly
    '''
    getch = Get()
    chbuff = input_to(getch)
    if chbuff:
        if chbuff =='q':
            defs.livesleft = -2
            time.sleep(0.2)
            print("\033[2J",end="")
            exit(0)
        elif chbuff in ['w','a','s','d']:
            defs.main_rider.move(chbuff)
            if chbuff=='w': defs.down=1
            else: defs.down=1
        elif chbuff == 'j':
            bullet.Bullet(defs.main_rider.xpos_left+defs.board_start+len(defs.main_rider.rider[0]),\
                defs.main_rider.ypos_top,2*int(defs.columns))
        elif chbuff == ' ':
            defs.main_rider.sheild() 
    elif not defs.main_rider._isSheilded:
        defs.main_rider.change_rider(0)

if __name__=="__main__":
    '''
    Main wrapper function
    '''
    defs.main_rider = rider.Rider()
    defs.board_check = create_check()
    defs.board = create_board()
    stats.Stats.create_board()
    thread1 = threading.Thread(target=increase_strt, daemon=True)
    thread1.start()
    while defs.dragonlivesleft>=0 and defs.livesleft>=0 and not defs.isbossfight:
        input_handler()
        defs.main_rider.check_pos()
    if defs.isbossfight:
        print("",end=defs.reset_color+"\033[0;0f")
        call(["python3", "bossfight.py"])
    else:
        inp.pr_result(2)
        print('\033['+defs.rows+';'+defs.columns+'f'+defs.reset_color)