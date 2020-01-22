fo = open("temp.txt", "r")
print("import defs")
print("col_df='\\x1b[38;2;33;160;8m'")
print("col_db='\\x1b[48;2;33;160;8m'")

lines = fo.readlines()
# This is 5th line
print('dragon = [')
for line in lines:
    print('\t[')
    for char in line[:-1]:
        if char!='█':
            val=-1
        else: 
            val = 1
        if char==' ':
            print("\t\t['','','"+char+"','',"+str(val)+"]",end=',\n')
        elif char=='*':
            print("\t\t['\x1B[31m',col_db,'◢','',1]",end=',\n')
        elif val==-1:
            print("\t\t[col_df,'','"+char+"','',"+str(val)+"]",end=',\n')
        else:
            print("\t\t[col_df,col_db,'"+char+"','',"+str(val)+"]",end=',\n')
        # print("'"+char+"'")
    print('\n\t],')
print(']')
print("for x in dragon:\n\tfor y in x:\n\t\tval=''\n\t\tfor p in y:\n\t\t\tif type(p)!=int:\n\t\t\t\tval+=p\n\t\tprint(val,end=defs.reset_color)\n\tprint()")