import defs
enemy = [
            ['\x1b[38;2;224;172;172m', '\x1b[48;2;0;0;0m', '▅', '', 1],
            ['\x1b[38;2;0;0;0m', '', '█', '', -1],
            ['\x1b[38;2;0;0;0m', '', '▐', '', -1]
        ]

for i in enemy:
    val=''
    for j in i:
        if type(j) != int:
            val+=j
    print(val+defs.reset_color)