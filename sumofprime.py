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
    
prime =[x for x in range(2,1000000) if (isPrime(x))]

val =0
valid=[]

for i in prime:
    val=val+i
    if(isPrime(val)):
        if(val<=)
        valid.append(val)

print(valid)