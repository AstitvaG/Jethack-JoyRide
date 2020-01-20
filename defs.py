import os
rows, columns = os.popen('stty size', 'r').read().split()
reset_color="\x1B[0m"
block = "\u2588"
bg = "\x1B[46m"
fg = "\x1B[36m"
col_sf = "\x1B[97m"
col_sb = "\x1B[107m"
board = list()
plain_board = list()
board_len = 4000
board_check = list()
board_start = 0
speed = 0.1
def_speed = speed