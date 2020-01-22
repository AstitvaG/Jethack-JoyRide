import defs
valx=40
valy=7
wf = "\x1B[37m"
wb = "\x1B[47m"
bf = "\x1B[30m"
bb = "\x1B[40m"
class Stats:
    score_board=[]
    rangex=range(int(defs.columns)//2-valx//2,int(defs.columns)//2+valx//2)
    rangey=range(1,1+valy)

    @staticmethod
    def create_board():
        for y in range(valy):
            temp=[]
            for x in range(valx):
                if (x==0 and y==0):
                    temp.append([bf,'','▗',''])
                elif (y==valy-2 and x==valx-2):
                    temp.append([bf,wb,'▗',''])
                elif (x==valx-1 and y==0):
                    temp.append([bf,'','▖',''])
                elif (y==valy-2 and x==1):
                    temp.append([bf,wb,'▖',''])
                elif (x==0 and y==valy-1):
                    temp.append([bf,'','▝',''])
                elif (y==1 and x==valx-2):
                    temp.append([bf,wb,'▝',''])
                elif (x==valx-1 and y==valy-1):
                    temp.append([bf,'','▘',''])
                elif (y==1 and x==1):
                    temp.append([bf,wb,'▘',''])
                elif x==0 or x==valx-1 or y==0 or y==valy-1:
                    temp.append([bf,'','█',''])
                else:
                    temp.append(['',wb,' ',defs.reset_color])
            Stats.score_board.append(temp)

    @staticmethod
    def print_f(i,j):
        if defs.oncePrinted:
            print("\033[1C",end='')
            return
        else:
            ix=Stats.rangey.index(i)
            iy=Stats.rangex.index(j)
            val = Stats.score_board[ix][iy][0]\
                 +Stats.score_board[ix][iy][1]\
                 +Stats.score_board[ix][iy][2]\
                 +Stats.score_board[ix][iy][3]
            val+=defs.bg+defs.fg
            print(val,end="")