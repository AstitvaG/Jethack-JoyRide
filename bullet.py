import defs,threading,time
class Bullet:
    bullet = ['\x1B[30m','','🡆',defs.bg+defs.bg]
    strt_posx=0
    posx=0
    posy=0
    rangex=0
    def __init__(self,startx,starty,rangex):
        defs.bulletsFired+=1
        self.strt_posx=startx
        self.posx=startx
        self.posy=starty
        self.rangex=rangex
        if self.posy < 0:
            self.posy=0
        defs.board_check[starty][startx] = 9
        threadx = threading.Thread(target=self.change_val, daemon=True)
        threadx.start()
    __savetemp = -1  
    def change_val(self):
        while(self.posx-self.strt_posx<self.rangex):
            if self.__savetemp==-1:
                defs.board_check[self.posy][self.posx] = 0
            else:
                defs.board_check[self.posy][self.posx] = self.__savetemp
            self.posx+=1
            if self.posx>defs.board_len-1 or self.posy==0:
                break
            if defs.board_check[self.posy][self.posx-defs.enemyrelpos] ==6:
                defs.enemiesKilled+=1
                self.clearArcs(self.posx-defs.enemyrelpos,self.posy,6)
                break
            if defs.board_check[self.posy][self.posx-defs.enemyrelpos+1] == 8:
                defs.enemiesKilled+=1
                self.clearArcs(self.posx-defs.enemyrelpos+1,self.posy,8)
                break
            if defs.board_check[self.posy][self.posx] == 1:
                self.clearArcs(self.posx,self.posy)
                break
            self.__savetemp = defs.board_check[self.posy][self.posx]
            defs.board_check[self.posy][self.posx] = 9
            time.sleep(defs.speed/6)
        else:
            defs.board_check[self.posy][self.posx] = 0
            
    @staticmethod
    def clearArcs(posx,posy,val=1):
        q1 = list()
        q2 = list()
        q1.append(posx) 
        q2.append(posy)
        while(len(q1)!=0):
            x=q1.pop(0)
            y=q2.pop(0)
            if defs.board_check[y][x]==0:
                continue
            defs.board_check[y][x]=0
            if(defs.board_check[y-1][x]<=val):
                q1.append(x)
                q2.append(y-1)
            if(defs.board_check[y+1][x]<=val):
                q1.append(x)
                q2.append(y+1)
            if(defs.board_check[y][x-1]<=val):
                q1.append(x-1)
                q2.append(y)
            if(defs.board_check[y][x+1]<=val):
                q1.append(x+1)
                q2.append(y)
            if(defs.board_check[y+1][x+1]<=val):
                q1.append(x+1)
                q2.append(y+1)
            if(defs.board_check[y+1][x-1]<=val):
                q1.append(x-1)
                q2.append(y+1)
            if(defs.board_check[y-1][x+1]<=val):
                q1.append(x+1)
                q2.append(y-1)
            if(defs.board_check[y-1][x-1]<=val):
                q1.append(x-1)
                q2.append(y-1)

        # pass

    @staticmethod
    def fill_in():
        return ['\x1B[30m','','🡆',defs.fg+defs.bg]