spisok = [10, 40, 20, 30]
# for element in spisok:
#     print(element + 2)
# print(range(0,len(spisok)))
# for i in range(len(spisok)):
#     # print(i)
#     print(spisok[i])
# for i in enumerate(spisok):
#     print(i)
# for id, val in enumerate(spisok):
#     print(id, val)
r_obj = range(len(spisok))
e_obj = enumerate(spisok)
for i in r_obj:
    if i == 1:
        break
# for i in e_obj:
#  if i[0] == 1:
#     break

#  for i in r_obj:
#     print(i)

# for i in e_obj:
#  print(i)
print(e_obj)