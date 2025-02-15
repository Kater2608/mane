# a = []
# for i in range(10):
#     a.append(i+1)
# print(a)

# import random
# a = []
# for i in range(10):
#     a.append(random.random())
# print(a)

# a = [i+1 for i in range(10)]
# # print(a)

# b = (i+1 for i in range(10)) #NO
# print(b)

# c = {i+1 for i in range(10)}
# print(c)

# d = {str(i+1):i+1 for i in range(10)}
# print(d)

# spisok=[1,2,3,4,5,6,7,8,9,10]
# for i in enumerate(spisok):
#     print(i)

# c = [(i+1, (i+1)/2) for i in range(4)]
# print(c)

# c=[(1, 0.5), (2, 1.0), (3, 1.5), (4, 2.0)]
# d = [i+j for i, j in c]
# print(d)

# s1 = 'abcd'
# s2 = '0123456789'
# d=[i+j for i in s1 for j in s2]
# print(d)

# a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b=[i for i in a if i%2==0]
# print(b)

# a = [1, 2, 3]
# b = [4, 5, 6]
# c=[(i,j) for i in a for j in b if i*j <= 10]
# print(c)

import random
# a = []
# for i in range(10):
#     a.append(random.randint(0,1000))
# print(a)

# a=[i for i in range(0,100,17)]
# print(a)

# count=0
# a=[23,-6,78,4,-789,-9,3,-45]
# for element in a:
#     if element<0:
#         count+=1       
# print(count)

# c=[]
# b=[]
# for i in range(5):
#     a=str(input("Введите слово: "))
#     c.append(a)
#     b.append(len(a))
# print(c)
# print(b)


# c=[]
# s1 = 'abcd'
# s2 = '01'
# for i in s1:
#     for j in s2:
#         a=i+j
#         c.append(a)
# print(c)

# a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in a:
#     if i%2==0:
#         print(i)

# a = [1, 2, 3]
# b = [4, 5, 6]
# for i in a:
#     for j in b:
#         if i*j <= 10:
#             print((i,j))

a= []
while True:
  b= input("Напиши слово (или 'хватит'): ")
  if b== "хватит":
    break
  else:
    a.append(b)
print("Вот слова:", a)
c = []
for i in a:
  try:
    v = float(i)
    c.append(v)
  except:
    print(i, "не число")
print("Вот числа:", c)