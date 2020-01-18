import os
rows, columns = os.popen('stty size', 'r').read().split()
reset_color="\x1B[0m"
block = "\u2588"
bg = "\x1B[46m"
fg = "\x1B[36m"
board = list()
plain_board = list()
board_len = 1070
board_check = list()
board_start = 0