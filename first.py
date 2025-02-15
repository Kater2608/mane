"""
print("hello ", name)
from random import randint
n = randint(1,3)
nastroenie =int(input("Оцени свое настроение от 1 до 10"))
if nastroenie > 5 and nastroenie <=7:
    print("У тебя неплохое настроение")
elif nastroenie<=5 :
    print("У тебя плохое настроение")
else:
    print("У тебя отличное настроение")"""

"""name = str(input("какое имя у тебя? "))
name1 = "Dima"
password1 = "12345"
name2 = "Alice"
password2 = "898989"
name3 = "Mary"
password3 = "101010"
name4 = "Saha"
password4 = "111111"
name5 = "Nastya"
password5 = "777777"

if name1 == name:
    if passsword1 == str(input("Введите пароль: ")):
        print (name1,", Вы вошли")
    else:
        print("Не правильный пароль")
elif  name2 == name:
    if passsword2 == str(input("Введите пароль: ")):
        print (name2,", Вы вошли")
    else:
        print("Не правильный пароль")
elif  name3 == name:
    if passsword3 == str(input("Введите пароль: ")):
        print (name3,", Вы вошли")
    else:
        print("Не правильный пароль")
elif  name4 == name:
    if passsword4 == str(input("Введите пароль: ")):
        print (name4,", Вы вошли")
    else:
        print("Не правильный пароль")
elif  name5 == name:
    if passsword5 == str(input("Введите пароль: ")):
        print (name5,", Вы вошли")
    else:
        print("Не правильный пароль") """


name1 ="Как называются животные,которое выкармливают детёнышей молоком?"
passsword1 = "Млекопитающие"
name2 ="Как называютсся животные состоящие из одной клетки?"
passsword2 ="Одноклеточные"
name3 ="Кто здесь лишний?Амёба,Человек,Кот,Лягушка"
passsword3 ="Амёба"
name4 ="Чем питаются комары?"
passsword4 ="Кровью"
name5 ="Что есть у позвоночных,чего нет у безпозвоночных?"
passsword5 ="Позвоночник"
name6 ="Вопрос жизни и смерти...тОрты или тортЫ?"
passsword6 ="тОрты"

col = 0




print("Привет,это Викторина из 6 вопросов по тематике животных.")
print("Как называются животные,которое выкармливают детёнышей молоком?")
passsword = str(input("Ответ: "))
if passsword1.lower() == passsword.lower():
    print ("Верно")
    col+=1
else:
    print("Не верно")
    

print("Как называютсся животные состоящие из одной клетки?")
passsword = str(input("Ответ: "))
if passsword2.lower() == passsword.lower():
    print ("Верно")
    col+=1
else:
    print("Не верно")
    
print("Кто здесь лишний?Амёба,Человек,Кот,Лягушка?")
passsword = str(input("Ответ: "))
if passsword3.lower() == passsword.lower():
    print ("Верно")
    col+=1
else:
    print("Не верно")


print("Чем питаются комары?")
passsword = str(input("Ответ: "))
if passsword4.lower() == passsword.lower():
    print ("Верно")
    col+=1
else:
    print("Не верно")

print("Что есть у позвоночных,чего нет у безпозвоночных?")
passsword = str(input("Ответ: "))
if passsword5.lower() == passsword.lower():
    print ("Верно")
    col+=1
else:
    print("Не верно")

print("Вопрос жизни и смерти...тОрты или тортЫ?")
passsword = str(input("Ответ: "))
if passsword6.lower() == passsword.lower():
    print ("Верно")
    col+=1
else:
    print("У меня нет слов...")

    
print("Количество праильны ответов", col)





    




    




