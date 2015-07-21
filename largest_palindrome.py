#!/usr/bin/env python3

def isPalindrom(val):
    #val = valu.split()
    lav = val[::-1]
    #print(lav, val)
    if( val == lav):

        return True


isPalindrom("9009")
palAray =[]
for i in range(100,999):
    for j in range(100,999):
        if(isPalindrom(str(j*i))):
            palAray.append(j*i)


print(sorted(palAray))