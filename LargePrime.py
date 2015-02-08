#!/usr/bin/env python3

import MilunPrime

def ListPrime(n):
    myList =[]

    i = 1

    while(True):
        i=i+1

        if(MilunPrime.MilunPrime.isPrime(i)==True):
            if(n%i ==0):
                #print(i)
                myList.append(i)
                result = n/i
                if(result == 1):
                    break
                else:
                    #print(result)
                    ListPrime(result)


    return  myList


print(ListPrime(13195))
