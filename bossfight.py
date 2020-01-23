import defs,rider,dragon,bullet,threading,time,copy,stats,coins,inp
from input import input_to, Get
from clouds import add_element

class BossFight:
    __main_riderf = rider.Rider()
    __main_dragon = dragon.Dragon()
    defs.isbossfight=True

    def print_board(self):
        print("",end="\033[0;0f")
        for i in range(int(defs.rows)):
            for j in range(int(defs.columns)):
                val=""
                if (i in stats.Stats.rangey) and (j in stats.Stats.rangex):
                    if defs.oncePrinted:
                        print("\033[1C",end='')
                        continue
                    else:
                        ix=stats.Stats.rangey.index(i)
                        iy=stats.Stats.rangex.index(j)
                        val = stats.Stats.score_board[ix][iy][0]\
                                +stats.Stats.score_board[ix][iy][1]\
                                +stats.Stats.score_board[ix][iy][2]\
                                +stats.Stats.score_board[ix][iy][3]
                        val+=defs.bg+defs.fg
                        print(val,end="")
                elif (i in self.__main_riderf.art_areay) and (j in self.__main_riderf.art_areax):
                    ix=self.__main_riderf.art_areay.index(i)
                    iy=self.__main_riderf.art_areax.index(j)
                    if self.__main_riderf.rider[ix][iy][4] == 1:
                        for x in self.__main_riderf.rider[ix][iy]:
                            if(type(x)!=int):
                                val+=x
                    else:
                        val = self.__main_riderf.rider[ix][iy][0]\
                                +defs.board[i][j][1]\
                                +self.__main_riderf.rider[ix][iy][2]\
                                +self.__main_riderf.rider[ix][iy][3]
                    val+=defs.bg+defs.fg
                    print(val,end="")
                elif (i in self.__main_dragon.art_areay) and (j in self.__main_dragon.art_areax):
                    ix=self.__main_dragon.art_areay.index(i)
                    iy=self.__main_dragon.art_areax.index(j)
                    if self.__main_dragon.dragon[ix][iy][2]!=' ':
                        defs.board_check[i][j]=1
                    if self.__main_dragon.dragon[ix][iy][4] == 1:
                        for x in self.__main_dragon.dragon[ix][iy]:
                            if(type(x)!=int):
                                val+=x
                    else:
                        val = self.__main_dragon.dragon[ix][iy][0]\
                                +defs.board[i][j][1]\
                                +self.__main_dragon.dragon[ix][iy][2]\
                                +self.__main_dragon.dragon[ix][iy][3]
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
        if not defs.oncePrinted:
            defs.oncePrinted=True
        self.print_values()

    
    def print_values(self):
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
        print("Boss:",defs.dragonlivesleft,end='')
        pos1y+=2
        print("",end="\033["+str(pos1y)+";"+str(pos1x)+"f"+stats.wb+stats.bf)
        print("Score:",defs.coinsCollected+2*defs.enemiesKilled,end='')
        print("",end=defs.reset_color+"\033[0;0f",flush=True)

    def create_board(self):
        board = list()
        for i in range(int(defs.rows)):
            temp_list = list()
            for _ in range(int(defs.columns)):
                if(i==0):
                    add_element(temp_list,fn=34)
                elif(i==int(defs.rows)-1):
                    add_element(temp_list,fn=32)
                else:
                    add_element(temp_list,cont=1)
            board.append(temp_list)
        return board

    def create_check(self):
        board_check = list()
        for _ in range(int(defs.rows)):
            temp_list = list()
            for _ in range(int(defs.columns)):
                temp_list.append(0)
            board_check.append(temp_list)
        return board_check

    def gameplay(self):
        if defs.start_time==-5:
            defs.start_time=time.time()
        start_time = time.time()
        grav_time=time.time()
        while defs.dragonlivesleft>=0 and defs.livesleft>=0:
            defs.board_check = copy.deepcopy(self.create_check())
            self.__main_riderf.move('s',val=defs.down)
            self.__main_dragon.move('s',val=defs.down)
            if time.time()-grav_time >defs.def_speed:
                defs.down+=1
                grav_time=time.time()
            if time.time()-start_time >0.3:
                bullet.Bullet(self.__main_dragon.xpos_left,\
                    self.__main_riderf.ypos_top,2*int(defs.columns),True,30)
                bullet.Bullet(self.__main_dragon.xpos_left-3,\
                    self.__main_riderf.ypos_top,2*int(defs.columns),True,30)
                bullet.Bullet(self.__main_dragon.xpos_left-2,\
                    self.__main_riderf.ypos_top+1,2*int(defs.columns),True,30)
                bullet.Bullet(self.__main_dragon.xpos_left-5,\
                    self.__main_riderf.ypos_top+2,2*int(defs.columns),True,30)
                start_time = time.time()
            self.print_board()
            time.sleep(defs.speed)

    def __init__(self):
        defs.board = self.create_board()
        defs.board_check = copy.deepcopy(self.create_check())
        defs.board_start = 0
        stats.Stats.create_board()
        defs.speed=defs.def_speed
        self.__main_riderf.ypos_top=int(defs.rows)-4
        thread1 = threading.Thread(target=self.gameplay,daemon=True)
        thread1.start()
        while defs.dragonlivesleft>=0 and defs.livesleft>=0:
            getch = Get()
            chbuff = input_to(getch)
            if chbuff:
                if chbuff =='q':
                    exit(0)
                elif chbuff in ['w','s']:
                    self.__main_riderf.move(chbuff)
                    self.__main_dragon.move(chbuff)
                    if chbuff=='w':
                        defs.down=0
                elif chbuff in ['a','d']:
                    self.__main_riderf.move(chbuff)
                elif chbuff == 'j':
                    bullet.Bullet(self.__main_riderf.xpos_left+len(self.__main_riderf.rider[0]),\
                        self.__main_riderf.ypos_top,int(defs.columns))
                elif chbuff == ' ':
                    self.__main_riderf.sheild() 
            elif not self.__main_riderf._isSheilded:
                self.__main_riderf.change_rider(0)
            self.__main_riderf.check_pos()
        if defs.livesleft>=0:
            inp.pr_result(1)
        else:
            inp.pr_result(2)
        print('\033['+defs.rows+';'+defs.columns+'f'+defs.reset_color)
BossFight()