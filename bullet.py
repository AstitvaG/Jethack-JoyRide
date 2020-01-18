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
        defs.board_check[starty][startx] = 9
        threadx = threading.Thread(target=self.change_val, daemon=True)
        threadx.start()
    def change_val(self):
        while(self.posx-self.strt_posx<self.rangex):
            time.sleep(defs.speed/2)
            defs.board_check[self.posy][self.posx] = 0
            self.posx+=1
            defs.board_check[self.posy][self.posx] = 9
        else:
            defs.board_check[self.posy][self.posx] = 0
    def chack_val(self):
        pass
    @staticmethod
    def fill_in():
        return ['\x1B[30m','','🡆',defs.fg+defs.bg]