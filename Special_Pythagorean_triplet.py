#!/usr/bin/env python3
# a+b+c=1000; c=1000-b-a; a<b

for b in range(2,1000):
    for a in range(1,b):
        c=1000-b-a
        if((a**2 + b**2)==c**2):
            print(a,b,c,a*b*c)

