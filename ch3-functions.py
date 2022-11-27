# functions

#default function
def func1():
    print("default function")

#function with parameters
def func2(arg1, arg2):
    print(arg1, " arg2:", arg2)

#function with parameters assigned
def func3(num, loopnum):
    result = 1
    for i in range(loopnum):
     print(i,loopnum)
     result = result * num
     print(result)
    return result
#function with multiple number of arguments defined in func call
def func4(*args):
    sumval = 0
    for i in args:
        print(i,args)
        sumval= sumval + i   
    return sumval

func1()
print(func1())

func2(2,3)
print(func3(2,3))

print(func2(arg1=3, arg2=5 ))

print(func4(1,3,5,7))



