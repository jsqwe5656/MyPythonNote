# -*- coding: utf-8 -*-

import struct

def isbmp(file):
    with open(file,'rb') as f:
        filehead = struct.unpack('<ccIIIIIIHH', f.read(30))
        if filehead[0] == b'B' and filehead[1] == b'M':
            print("{} is bmp file.".format(file))
            print("Its size is {}".format(filehead[9]))
        else:
            print("%s is not a bmp file." % file)
            print(filehead[0] + filehead[1])

if __name__=="__main__":
    filename = input('文件名称')
    isbmp(filename)