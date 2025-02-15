import random
spisok=[]
a=input()
b=input()
if a>b:
    c=a
    a=b
    b=c
try:
    a=float(a)
    b=float(b)
except TypeError:
    print("No")
else:
    for i in range(20)
    if a%1==0 and b%1==0:
        print(random.randrange(a,b))
    else:
        print(round(random.random()* (b-a)* a,3))