import defs,rider,dragon,bullet,threading,time,copy
from input import input_to, Get
from clouds import add_element

main_rider = rider.Rider()
main_dragon = dragon.Dragon()
defs.isbossfight=True
def print_board():
    print("",end="\033[0;0f")
    for i in range(int(defs.rows)):
        for j in range(int(defs.columns)):
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
                            +defs.board[i][j][1]\
                            +main_rider.rider[ix][iy][2]\
                            +main_rider.rider[ix][iy][3]
                val+=defs.bg+defs.fg
                print(val,end="")
            elif (i in main_dragon.art_areay) and (j in main_dragon.art_areax):
                ix=main_dragon.art_areay.index(i)
                iy=main_dragon.art_areax.index(j)
                if main_dragon.dragon[ix][iy][2]!=' ':
                    defs.board_check[i][j]=1
                if main_dragon.dragon[ix][iy][4] == 1:
                    for x in main_dragon.dragon[ix][iy]:
                        if(type(x)!=int):
                            val+=x
                else:
                    val = main_dragon.dragon[ix][iy][0]\
                            +defs.board[i][j][1]\
                            +main_dragon.dragon[ix][iy][2]\
                            +main_dragon.dragon[ix][iy][3]
                val+=defs.bg+defs.fg
                print(val,end="")
            elif defs.board_check[i][j] in [9,30]:
                b = bullet.Bullet.fill_in(defs.board_check[i][j])
                print(b[0]+defs.board[i][j][1]+b[2]+b[3],end="")
            else:
                for x in defs.board[i][j]:
                    val+=x
                print(val,end="")
        if i!=int(defs.rows)-1 and j!=int(defs.columns)-1:
            print()
        else:
            print("",end="")
    print(defs.reset_color,end="",flush=True)
    print("",end="\033[0;0f")
    print(defs.reset_color,defs.coinsCollected,defs.enemiesKilled,defs.bulletsFired,defs.livesleft,defs.dragonlivesleft)

def create_board():
    board = list()
    for i in range(int(defs.rows)):
        temp_list = list()
        for _ in range(int(defs.columns)):
            if(i==0):
                add_element(temp_list,fn=34)
            elif(i==1):
                add_element(temp_list,fn=34)
            elif(i==int(defs.rows)-1):
                add_element(temp_list,fn=32)
            else:
                add_element(temp_list,cont=1)
        board.append(temp_list)
    return board

def create_check():
    board_check = list()
    for _ in range(int(defs.rows)):
        temp_list = list()
        for _ in range(int(defs.columns)):
            temp_list.append(0)
        board_check.append(temp_list)
    return board_check


def gameplay():
    start_time = time.time()
    while defs.dragonlivesleft>=0 and defs.livesleft>=0:
        defs.board_check = copy.deepcopy(create_check())
        if time.time()-start_time >0.3:
            bullet.Bullet(main_dragon.xpos_left,\
                main_rider.ypos_top,int(defs.columns),True,30)
            bullet.Bullet(main_dragon.xpos_left-10,\
                main_rider.ypos_top,int(defs.columns),True,30)
            bullet.Bullet(main_dragon.xpos_left,\
                main_rider.ypos_top+1,int(defs.columns),True,30)
            bullet.Bullet(main_dragon.xpos_left-10,\
                main_rider.ypos_top+1,int(defs.columns),True,30)
            start_time = time.time()
        print_board()
        time.sleep(defs.speed)


defs.board = create_board()
defs.board_check = copy.deepcopy(create_check())
defs.board_start = 0
thread1 = threading.Thread(target=gameplay,daemon=True)
thread1.start()
while defs.dragonlivesleft>=0 and defs.livesleft>=0:
    getch = Get()
    chbuff = input_to(getch)
    if chbuff:
        if chbuff =='q':
            exit(0)
        elif chbuff in ['w','s']:
            main_rider.move(chbuff)
            main_dragon.move(chbuff)
        elif chbuff in ['a','d']:
            main_rider.move(chbuff)
        elif chbuff == 'j':
            bullet.Bullet(main_rider.xpos_left+len(main_rider.rider[0]),\
                main_rider.ypos_top,int(defs.columns))
        elif chbuff == ' ':
            main_rider.sheild() 
    elif not main_rider._isSheilded:
        main_rider.change_rider(0)
    main_rider.check_pos()