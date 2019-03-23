from functools import *
arr=list()
len=0

def chkPrime(no):
    i=int((no/2))+1
    while(i>1):
        if(no%i==0):
            break
        i-=1
    if(i==1):
        return True
    else:
        return False

def InitList():
    len=input("Enter number of elements:")
    for i in range(0,len):
        arr.append(input("Enter element at index {} :".format(i)))
    return

InitList()
Arr2= list(map(lambda no:(no*2),filter(chkPrime,arr)))
iResult=int(reduce(max,Arr2))
print(arr)
print(Arr2)
print(iResult)