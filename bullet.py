import defs,threading,time
class Bullet:
    bullet = ['\x1B[30m','','🡆',defs.bg+defs.bg]
    strt_posx=0
    posx=0
    posy=0
    rangex=0
    def __init__(self,startx,starty,rangex):
        self.strt_posx=startx
        self.posx=startx
        self.posy=starty
        self.rangex=rangex
        if self.posy < 0:
            self.posy=0
        defs.board_check[starty][startx] = 9
        threadx = threading.Thread(target=self.change_val, daemon=True)
        threadx.start()
        
    def change_val(self):
        while(self.posx-self.strt_posx<self.rangex):
            defs.board_check[self.posy][self.posx] = 0
            self.posx+=1
            if self.posx>defs.board_len-1:
                break
            if defs.board_check[self.posy][self.posx] == 1:
                self.clearArcs(self.posx,self.posy)
                break 
            defs.board_check[self.posy][self.posx] = 9
            time.sleep(defs.speed/6)
        else:
            defs.board_check[self.posy][self.posx] = 0
    @staticmethod
    def clearArcs(posx,posy):
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
            if(defs.board_check[y-1][x]==1):
                q1.append(x)
                q2.append(y-1)
            if(defs.board_check[y+1][x]==1):
                q1.append(x)
                q2.append(y+1)
            if(defs.board_check[y][x-1]==1):
                q1.append(x-1)
                q2.append(y)
            if(defs.board_check[y][x+1]==1):
                q1.append(x+1)
                q2.append(y)
            if(defs.board_check[y+1][x+1]==1):
                q1.append(x+1)
                q2.append(y+1)
            if(defs.board_check[y+1][x-1]==1):
                q1.append(x-1)
                q2.append(y+1)
            if(defs.board_check[y-1][x+1]==1):
                q1.append(x+1)
                q2.append(y-1)
            if(defs.board_check[y-1][x-1]==1):
                q1.append(x-1)
                q2.append(y-1)

        # pass

    @staticmethod
    def fill_in():
        return ['\x1B[30m','','🡆',defs.fg+defs.bg]