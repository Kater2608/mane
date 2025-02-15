"""
old=int(input('Ваш возраст: '))
print('Рекомендовано: ', end=' ')
if 3<= old <6:
    print('"Заяц в лаберинте"')
if 6<= old <12:
    print('"Марсианин"')
if 12<= old <16:
    print('"Загадочный остров"')
if 16<= old:
    print('"Поток сознания"')
"""
"""
old = int(input('Ваш возраст: '))
print('Рекомендовано:', end=' ')
if 3 <= old < 6:
    print('"Заяц в лабиринте"')
else:
    if 6 <= old < 12:
        print('"Марсианин"')
    else:
        if 12 <= old < 16:
            print('"Загадочный остров"')
        else:
             if 16 <= old:
                 print('"Поток сознания"')
"""
"""
try:
    old = int(input('Ваш возраст: '))
except ValueError:
    print("Это не целое число")
else:
    if 3 <= old < 6:   
        print('"Заяц в лабиринте"')
    elif 6 <= old < 12:
        print('"Марсианин"')
    elif 12 <= old < 16:
        print('"Загадочный остров"')
    elif 16 <= old:
        print('"Поток сознания"')
    else:
        print("Такого нет")
"""
"""
a=int(input("Введите число: "))
if a>0:
      print("1")
elif a<0:
    print("-1")
else:
        print("0")
"""
    
