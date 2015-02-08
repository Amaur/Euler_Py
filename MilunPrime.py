#!/usr/bin/env python3
import math

class MilunPrime():
    def __init__(self,  value):
        self.lim = value

# method the verify if a number is prime
    @staticmethod
    def isPrime(n):
        j=1
        nracine = math.ceil( math.sqrt(n) )
        if ( n==2):
            return  True
        #elif(n%2==0):
         #   return  False
        else:
            while(j<nracine):
                j=j+1
                if(n%j==0):
                    return  False
                    break
                else:
                    continue

            return  True
# making the list of the prime number
    def primeNumber(self):
        lastPrime =0

        i=1
        count =0
        while(count < self.lim):
            i=i+1

            if( self.isPrime(i) ==True ):
                count = count +1
                if(lastPrime <i):
                    lastPrime =i


        print (lastPrime)
"""
# displaying the 10001th prime number
    def lastPrime(self):
        self.lastlist = self.primeNumber()

        print("The result is:", self.lastlist.pop()) """








if __name__=="__main__":
    myprime= MilunPrime(10001)
    myprime.primeNumber()
    #myprime.lastPrime()