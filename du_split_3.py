# coding: UTF-8
import sys

args = sys.argv
if len(args) == 1:
    drive_name = 'テスト'
else:
    drive_name = args[1]
    
#print(args)

path = 'x.txt'

f = open(path)

with open(path) as f:
    while True:
        s_line = f.readline()

#        if s_line == '\n':
#            break
        
        fd = s_line.find('du: Warning:')
        if fd == -1:
        #print(fd)
            #print(s_line, end='')
#改行で分割: splitlines
            s_new = ''.join(s_line.splitlines())
#            print(s_new)

#ディレクトリに .\ がつく仕様を利用してサイズとフォルダ名を分割            
            s_list = s_new.split('.\\')
            if len(s_list) == 2:
                #print(s_list)
                s_list[0] = int(s_list[0])
#アニメ の切り出し               
                fd2 = s_line.find('アニメ ')
                if fd2 != -1:
                    s_list2 = s_list[1].split()
#                    print(s_list2)
#                s_list[1] = str.strip(s_list[1])
#                print(s_list[0],',',s_list[1])
#                print(s_list[0],s_list[1])

#------------
#アウトプット
#------------
                print(drive_name,end='')
                print(',', end='')
                if fd2 != -1:
                    print(s_list2[0], end='')
                    print(',', end='')
                    print(s_list2[1], end='')
                else:
                    print('なし', end='')
                    print(',', end='')
                    print(s_list[1], end='')
                print(',', end='')
                print(s_list[0])
        if not s_line:
            break

f.close()
                                     