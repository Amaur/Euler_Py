def Factorial(n):
    fac = 1
    for x in range(1,n+1):
        fac=fac*x
    return fac

def FactSum(Num):
    sum =0
    for i in Num:
        sum = sum+int(i)
    return sum


facto = Factorial(100)
mySum = FactSum(str(facto))

print(mySum)