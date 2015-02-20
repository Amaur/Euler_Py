import math


class Prime_Factor():
    def __int__(self,nValue):
        self.m_nValue = nValue

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
    def search(self,m_nValue,n):
        if (m_nValue/n ==0)



