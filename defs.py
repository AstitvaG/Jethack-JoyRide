import os
rows, columns = os.popen('stty size', 'r').read().split()
reset_color="\x1B[0m"
block = "\u2588"
board = list()
bg = "\x1B[46m"
fg = "\x1B[36m"
block = "\u2588"
board_len = 10000