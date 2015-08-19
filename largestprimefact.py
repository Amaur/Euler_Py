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



def primfact(val):
    prime=[]
    div=1
    for i in range(2,math.ceil(val/div)):
        if(isPrime(i)):
            #print(i)
            if( val%i==0):
                div=i
                print(div)
                prime.append(i)
        if(functools.reduce(operator.mul,prime,1)==val):
            break
        else:
            continue


    print(prime)


primfact(600851475143)
#print(isPrime(130))