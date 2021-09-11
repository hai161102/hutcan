import math
a=float(input())
b=float(input())
c=float(input())

if a == 0:
    if b == 0:
        if c == 0:
            print( "pt vo so ng")
        else:
            print("pt vo ng")    
    else:
        print("pt co 1 ng x = ",+(-c/b));
delta = b*b -4 * a * c
if delta > 0:
    x1 = (float) ((-b + math.sqrt(delta))/(2*a))

    x2 = (float) ((-b - math.sqrt(delta))/(2*a))
        print("pt co 2 ng x1= " + x1 "x2= " + x2)
else(delta =0):
    x1=(-b/(2*a))
        print("pt co ng x1=x2= " + x1)
else:
        print("pt vo ng)