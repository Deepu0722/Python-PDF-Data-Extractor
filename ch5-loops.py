# python has only 2 types of loops while and for
#use while
x = 5
while x < 3:
    print(x)

#Use for loop  for a range of vals
for x in range(3, 10):
    print(x)

#Use for loop over a collection list
days = ["mon","tue","wed","thur"]
for x in days:
    print(x)

#Use for extracting index val use enumerate
for i,x in enumerate(days):
    print(i,x)

# USe break and continue
for x in range(3,10):
    if x == 7 :
     break  
    elif x % 2 == 0 :
     continue
    print (x)  


