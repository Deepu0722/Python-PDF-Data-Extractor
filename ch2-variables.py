#Basic data types in Python : strings, boolean, sequences, dictionaries
from operator import truediv


myint = 5
myfloat = 2.3
mystr = "String value"
mybool = True
mylist = [0, 1, "two", 3.2, False, 6, "hi"] #tuple
mytuple = (0, 1, 2)
mydict = {"one":1, "two": 1}

#redeclaring values works
myint = "new"
print("redeclare int to str : ",myint)

#to access a member of a sequence type , use []
print(mylist[1])
print(mylist[3])

#use slices to get parts of a sequence
print(mylist[1:3])
#slice to skip step value : 
# here it is every second value
print(mylist[1:7:2]) 

#slice to reverse the sequence
print(mylist[::-1])

#dictionaries are accessed via keys
print(mydict["two"])

# ERROR: variables of different type cannot ne combined
print("atring value" + str(123))

#Gloabal vs local variables in functions
def newfunction():
    global mystr # "global_keyword" will update value of mystr globally otherwise local value is updated
    mystr = "def"
    print (mystr)

newfunction() #explicit function call
print(mystr) 

# del keyword is used to delete/undefine variable
del mystr
print(mystr)
