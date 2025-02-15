"""
for i in range(10):
    print("Kate")
print("Ready")



for i in range(1):
    print("Red")
for i in range(20):
    print("Gold")    

for i in range(100):
    print ((i+1)*2)

total=0
total1=0
totalm=0
totalp=0

for i in range(7):
    newNumber= int(input("Введите число" ))
    total += newNumber
    if newNumber == 0:
        total1 += 1
    elif newNumber>0:
        totalp +=1
    else:
        totalm +=1
print("Сумма чисел: ",total)        
print("Вы ввели ноль ",total1, " раз")
print("Вы положительное число ",totalp, " раз")
print("Вы отрицательное число ",totalm, " раз")


a=0
b=5

if b>6:
    b=b-1
print (b)


a=0
b=5

for i in range(5):
    b=b-1
    print(b)



a=0
b=5
while b>0:
    b=b-1
print(b)
"""      
"""  
a=5
b=5

for i in range(5):
    a=a-1
    while b>0:
        b=b-2
print(b)
print(a)



s="Гидроэлектростанция"
print(str(s[2]))
print(str(s[-2]))
print(s[0:5])
print(s[0: -2])
print(s[::2])
print(s[1::2])
print(s[0::3])
print(s[::-1])
print(len(s))
"""
"""
s="Бобры живут в гидроэлектростанциии"
print (s.count(" ")+1)





s="Бобры живут в \
гидроэлектростанциии"
print(len(s))
s.replace("Бобры живут в ","гидроэлектростанциии")
s.replace("гидроэлектростанциии","Бобры живут в ")
print(s)







str="ijdfyueg@hgjsgxuyg@kdikdi@"
print("Исходная строка: " + str)
res_str = str.replace("@", '')
print("Без '@': " + res_str)
"""


"""
for i in range(5):
    print("Я не буду жевать жвачку в классе.")
"""
"""
for i in range(5):
    print("Please")
print("CanI go to the mall?")
"""
"""
for i in range(5):
    print("Please")
    print("CanI go to the mall?")
"""
"""
for i in range(10):
    print (i)
"""
"""
for i in range(1,11):
    print(i)
"""
"""
for  i in range(5):
    print ((i+1)*2)
"""
"""
for i in range(2,12,2):
    print(i)
"""
"""
for i in range(10):
    print(i+1)
"""
"""
for i in range(3):
    print("a")
for j in range(3):
    print("b")
"""
"""
for i in range(3):
    print("a")
    for j in range(3):
        print("b")
print("Ready")
"""
"""
total=0
for i in range(5):
    newNumber = int(input("Введите число"))
    total += newNumber
print("Сумма чисел: ",total)
"""
"""
sum=0
for i in range(1,101):
    sum=sum + i
print(sum)
"""
"""
total=0
for i in range(5):
    newNumber = int(input("Введите число: "))
    if newNumber == 0:
        total += 1
print("Вы ввели ноль",total," раз")
"""
"""
a=0
for i in range(10):
    a=a+1
print(a)
"""
"""
a=0
for i in range(10):
    a=a+1
for j in range(10):
    a=a+1
print(a)
"""
"""
a=0
for i in range(10):
    a=a+1
    for j in range(10):
        a=a+1
print(a)
"""

"""
s="Guess my number"
print(s)
"""
"""
s= "Hello! This is my mew game\
    Guess my number"
print(s)
"""
"""
print("Start:\n\tstring\n\tstring\n\tstring\nEnd")
"""
"""
s1 = "Hello"
s2 = "World"
print(s1+s2)
"""
"""
s1 = "Hello"
print(s1 * 10)
"""
"""
s1 = "Hello"
print(len(s1))
"""
"""
s= "Hello World"
print("symbol [0]: " + str(s[0]))
print("symbol [6]: " + str(s[6]))
"""
"""
s="Hello World"
i = len(s)
print(s[i])
"""
"""
s= "guEss mY numBer"
s.capitalize()
s.title()
s.upper()
s.lower()
"""
"""
s = "message"
s.find("m")
s.find("s")
s.find("w")
"""

"""
s= "message"
s.rfind("m")
s.rfind("s")
s.rfind("w")
"""
"""
s="best regards best"
s.replace("best","kind")
s.replase("best","kind", 1)
"""
"""
s="Hello World"
s.count("l"))
"""
"""
s="messeage"
print(s.rfind("s"))
print(s.count("s"))
print(s.find("e"))
print(s.replace("e", "",1))
print(s.find("e"))
"""
"""
a=5
while a<10:
    print("Now value of a: " + str(a)
          + ". But it is less than10!")
    a = a + 1
    print("Thats it! Now the number a is greater than 10!")
    """
"""
while True:
    break
"""
"""
col=1
a=int(input("Введите число"))
total=a
while a!=0:
    a=int(input("Введите число"))
    col+=1
    total+=a
print(col)
print(total)
"""

"""
a=11
while a<=29:
    print(a)
    a+=2
"""
"""
col=0
total=0
number =int(input("Введите число"))
while number !=0:
    col+=number
    total+=1
    number=int(input("Введите число"))
print(total/col)
"""
"""
a=int(input("Введите число"))
for i in range(a):
    print("*"*a)
"""
"""
a=0
while a<5:
    a+=1
    print("*" * a)
"""
"""
a=input("Введите значение: ")
b=input("Введите значение: ")
try:
     a=float(a)
     b=float(b)
     print(a+b)
except ValueError:
     print (str(a)+str(b))
else:
     print("Good")
finally:
     print("End")
"""
"""
def test():
     number =  int(input("Введите число"))
     if number < 0:
          negative()
     else:
          positive()
          
def positive():
     print("Положительное")
     
def negative():
     print("Отрицательное")
test()
"""
"""
PlohadCulindraKrug =0

def cylinder ():
     b=0

     while b==0:
          try:
               r=float(input("Введите радиус:"))
               h=float(input("Введите высоту"))
               b=1
               if r <=0 or h<=0:
                    b=0              
PlohadCulindraBokStorona=0
def circle():
     global PlohadCulindraKrug
     PlohadCulindraKrug =3.141592654 * r **2
     PlohadCulindraBokStorona=2*3.141592654*r*h
     a=input("Только боковая площадь 1.Вся площадь 2")
     b=0
while b==0:
     if a== "1" or a=="2":
          b=1
     else:
          print("Введите 1 или 2")
          a=input("Только боковая площадь 1.Вся площадь 2")
          b=0
if a =="1":
          print("Площадь боковой поверхности" / PlohadCulindraBokStorona)
     else:
          circle():
          print("Площадь всей фигуры" / (PlohadCulindraKrug+PlohadCulindraBokStorona * 2))
cylinder ()
          
"""
"""
def cylinder():
    r = float(input())
    h = float(input())
    # площадь боковой поверхности цилиндра:
    side = 2 * 3.14 * r * h
    # площадь одного основания цилиндра:
    circle = 3.14 * r**2
    # полная площадь цилиндра:
    full = side + 2 * circle
    return full
 
square = cylinder()
print(square)
"""
"""
def cylinder():
    try:
        r = float(input())
        h = float(input())
    except ValueError:
        return
    side = 2 * 3.14 * r * h
    circle = 3.14 * r**2
    full = side + 2 * circle
    return full
 
print(cylinder())
"""
"""
def xor(a,b) :
     g= ' '
     for i in range(len(a)):
          if a[i] !=b[i]:
               g=g+'1'
          else:
                  g=g+'0'
     return  g
a='011001010111110101010'
b='101011110101010100011'
print(xor(a,b))
"""
"""
def c():
     a=input()
     b=input()
     return a+b
print(c())
"""
"""
def a():
     itog=int(input())
     return 1 if itog == 0 else itog*a()
itog =a()
print(itog)
"""
"""
a=1
while a<=6:
    b=float(input("Введите 6 вещественных чисел"))
    if a == 1:
            min_b=b
            max_b=b
    else:
            if b>max_b:
                max_b=b
            elif b< min_b:
                min_b=b
    a +=1
print("Минимальное",round(min_b, 2))       
print("Максимальное", round(max_b,  2))
"""

"""
a=[]
for i in range(8):
    aa=int(input("Введите цифру"))
    a.append(aa)
    suma=sum(a)
    maxa=max(a)
    mina=min(a)
print(suma)
print(maxa)
print(mina)
"""
