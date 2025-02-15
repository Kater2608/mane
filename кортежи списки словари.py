"""
#Списки
a=[]
while len(a)< 8:
    a.append(int(input(" ")))
print(min(a))
print(max(a))
print(sum(a))
"""
"""
#Кортежи
Hmmmm=[1,3,56,9,0,"amogus",777]
Hmmmm_1=Hmmmm.copy()
Hmmmm_2=Hmmmm[:]
print(Hmmmm)
print(Hmmmm_1)
print(Hmmmm_2)
"""
"""
#Словари
school={"1а":25, "1б":50, "2б":100, "6а":2, "7в":0.5}
school["2б"]=101
school["100б"]=9
del school["1б"]
print(sum(school.values()))
print(school)
"""
"""
#Списки_2
import random
o= []
m= 0
while m < 100:
    a=(random.random())
    o.append(round(a, 2))
    m += 1
o.sort()
def spisok(d):
    m=0
    while m< 100:
        global o
        print(o[m:m+1])
        m+=10
spisok(o)
print(spisok)
"""
"""
a = open('C:/Users/NAIT/Desktop/субботняя группа/Карсонова/data.txt','r' )
b=a.readlines()
b2=[]
rus=["один","два","три","четыре","пять"]
eng=["one","two","three","four","five"]
c=0

for i in b:
    b2.append(i.replace(eng[c],rus[c]))
    c+=1
    a2=open('C:/Users/NAIT/Desktop/субботняя группа/Карсонова/dataRu.txt','w' )
    a2.writelines(b2)
    a2.close()
a.close()
print(b2)
"""

a=open("C:/Users/NAIT/Desktop/субботняя группа/Карсонова/nums.txt")
b=a.read()
b=b.split()
sum=0
for e in range(len(b)):
    sum+=int(b[e])
print(sum)


