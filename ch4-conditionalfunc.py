# contional function : loop : if elif else 
x, y = 7,5
if x < y :
    print("x is < y ")
elif x == y:
    print(" x is == y ")
else :
    print(" x > y ")  

#contional statement " a if C else b"
result = " x is < y " if x < y else "xis > y or = y "
print (result)

#contional statement match- case where x is compared with multiple val (switch)
value = "six"
match value:
    case "one":
        result = 1
    case "two":
        result = 2  
    case ("three"| "four"):
        result = (3,4)
    case _:
        result = -1
print (result)
