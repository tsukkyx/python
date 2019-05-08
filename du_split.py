# coding: UTF-8

path = 'x.txt'

f = open(path)

with open(path) as f:
    while True:
        s_line = f.readline()
        #print(s_line,']')
        fd = s_line.find('du: Warning:')
        if fd == -1:
        #print(fd)
            #print(s_line, end='')
            s_new = ''.join(s_line.splitlines())
            s_list = s_new.split('.\\')
            if len(s_list) == 2:
                #print(s_list)
                s_list[0] = int(s_list[0])
#                s_list[1] = str.strip(s_list[1])
#                print(s_list[0],',',s_list[1])
#                print(s_list[0],s_list[1])
                print(s_list[0], end='')
                print(',', end='')
                print(s_list[1])
        if not s_line:
            break


f.close()
                                     