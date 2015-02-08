def EvenFibo():
    suma =0

    currentFib , nextFibo =1,1

    while(nextFibo<=4000000):
        currentFib , nextFibo = nextFibo,nextFibo+currentFib

        if(nextFibo%2==0):
            suma =suma+nextFibo

    return suma



print( EvenFibo() )