import defs,threading,time,copy,elements
class Bullet(elements.Elements):
    __strt_posx=0
    __posx=0
    __posy=0
    __rangex=0
    __savetemp = -1

    def __init__(self,startx,starty,__rangex,back=False,val=9):
        if not back:
            defs.bulletsFired+=1
        self.__strt_posx=startx
        self.__posx=startx
        self.__posy=starty
        self.__rangex=__rangex
        if self.__posy < 0:
            self.__posy=0
        defs.board_check[starty][startx] = val
        threadx = threading.Thread(target=self.change_val,args=(back,val,), daemon=True)
        threadx.start()
    
    def change_val(self,back,val):
        while(self.__posx-self.__strt_posx<self.__rangex and self.__posx<len(defs.board[0])-2):
            if self.__savetemp==-1 or self.__savetemp==val:
                defs.board_check[self.__posy][self.__posx] = 0
            else:
                defs.board_check[self.__posy][self.__posx] = self.__savetemp
            if back:
                self.__posx-=1
                if self.__posx<0:
                    break
            else:
                self.__posx+=1
            if self.__posx>defs.board_len-1 or self.__posy==0:
                break
            if self.__posx-defs.enemyrelpos < defs.board_len-2:
                if defs.board_check[self.__posy][self.__posx-defs.enemyrelpos] ==6:
                    defs.enemiesKilled+=1
                    self.clearArcs(self.__posx-defs.enemyrelpos,self.__posy,6)
                    break
                if defs.board_check[self.__posy][self.__posx-defs.enemyrelpos+1] == 8:
                    defs.enemiesKilled+=1
                    self.clearArcs(self.__posx-defs.enemyrelpos+1,self.__posy,8)
                    break
            if defs.board_check[self.__posy][self.__posx] == 1:
                self.clearArcs(self.__posx,self.__posy,boss=defs.isbossfight)
                break
            self.__savetemp = defs.board_check[self.__posy][self.__posx]
            defs.board_check[self.__posy][self.__posx] = val
            if not back:
                time.sleep(defs.speed/6)
            else:
                time.sleep(defs.speed/6)
        else:
            defs.board_check[self.__posy][self.__posx] = 0
            
    @staticmethod
    def clearArcs(__posx,__posy,val=1,boss=False):
        q1 = list()
        q2 = list()
        q1.append(__posx) 
        q2.append(__posy)
        while(len(q1)!=0):
            x=q1.pop(0)
            y=q2.pop(0)
            if defs.board_check[y][x]==0:
                continue
            defs.board_check[y][x]=0
            try:
                if(defs.board_check[y-1][x]<=val):
                    q1.append(x)
                    q2.append(y-1)
            except: pass
            try:
                if(defs.board_check[y+1][x]<=val):
                    q1.append(x)
                    q2.append(y+1)
            except: pass
            try:
                if(defs.board_check[y][x-1]<=val):
                    q1.append(x-1)
                    q2.append(y)
            except: pass
            try:
                if(defs.board_check[y][x+1]<=val):
                    q1.append(x+1)
                    q2.append(y)
            except: pass
            try:
                if(defs.board_check[y+1][x+1]<=val):
                    q1.append(x+1)
                    q2.append(y+1)
            except: pass
            try:
                if(defs.board_check[y+1][x-1]<=val):
                    q1.append(x-1)
                    q2.append(y+1)
            except: pass
            try:
                if(defs.board_check[y-1][x+1]<=val):
                    q1.append(x+1)
                    q2.append(y-1)
            except: pass
            try:
                if(defs.board_check[y-1][x-1]<=val):
                    q1.append(x-1)
                    q2.append(y-1)
            except: pass
        if boss == True:
            defs.dragonlivesleft-=1

    @staticmethod
    def fill_in(val):
        if val==9:
            return ['\x1B[38;2;136;136;136m','','🡆',defs.fg+defs.bg]
        else:
            return ['\x1b[38;2;255;165;0m','','█',defs.fg+defs.bg]

    @staticmethod
    def check_x(i,j):
        return defs.board_check[i][j] in [9,30]

    @staticmethod
    def print_f(i,j):
        b = Bullet.fill_in(defs.board_check[i][j])
        print(b[0]+defs.plain_board[i][j][1]+b[2]+b[3],end="")