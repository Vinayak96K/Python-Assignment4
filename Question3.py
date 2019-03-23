from functools import *
arr=list()
len=None

def InitList():
    len=input("Enter number of elements:")
    for i in range(0,len):
        arr.append(input("Enter element at index {} :".format(i)))
    return

InitList()
newArr = list(map(lambda no:no+10,filter(lambda no: (no>=70 and no<=90),arr)))
iResult=int(reduce(lambda no1,no2: (no1*no2),newArr))
print(arr)
print(newArr)
print(iResult)