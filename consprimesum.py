import math
import functools
import operator

def isPrime(n):
    j=1
    nracine = math.ceil(math.sqrt(n))
    #print(nracine)
    if(n==2):
        return (True)
    else:

        while(j<nracine):
            j=j+1
            if(n%j==0):
                return ( False)
                break
            else:
                continue
        return (True)

prime =[]

for i in range(2,2000000):
    if(isPrime(i)):
        #print(i)
        prime.append(i)

print(prime)