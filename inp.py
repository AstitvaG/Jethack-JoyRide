import stats,defs

stats.Stats.create_board()
def pr_result(valx=1):
    for i in stats.Stats.rangey:
        for j in stats.Stats.rangex:
            ix=stats.Stats.rangey.index(i)
            iy=stats.Stats.rangex.index(j)
            val = defs.bg+defs.fg\
                +stats.Stats.score_board[ix][iy][0]\
                +stats.Stats.score_board[ix][iy][1]\
                +stats.Stats.score_board[ix][iy][2]\
                +stats.Stats.score_board[ix][iy][3]
            print("",end="\033["+str(i+1)+";"+str(j+1)+"f")
            print(val,end="")
    print('',end='',flush=True)
    if valx==1:
        fo = open("win.txt", "r")
    else:
        fo = open("lose.txt", "r")
    lines = fo.readlines()
    i=stats.Stats.rangey[0]+1
    j=stats.Stats.rangex[0]+stats.valx//2-(len(lines[0])+1)//2
    for line in lines:
        print("",end="\033["+str(i+1)+";"+str(j+1)+"f"+stats.wb+stats.bf)
        print(line,end='')
        i+=1
    print()