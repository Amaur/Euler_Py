"""li = list(range(2,21))
print(li)

i=0
j=10 """

"""
while(i<len(li)):
    if(j%li[i]==0):
        i=i+1
        #continue
    else:
        j=j+5
        i=0
print(j)

"""

def Small(j):
    limnumber = list(range(2,j+1))
    i=0
    value=10
    while(i<len(limnumber)):
        #print(len(limnumber))
        if(value%limnumber[i]==0):
            i=i+1
        else:
            value=value+5
            i=0

    return value


#value =10
print(Small(20))