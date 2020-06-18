
#Попросить пользователя ввести текст. В результате вывести % букв в верхнем регистре и в нижнем регистре. 

name=input("Введите пожалуйста текст ")
upper_letters=0 #это просто название можно любое написать
lower_letters=0
for i in list(name):
    if i.isupper():
        upper_letters=upper_letters+1
    elif i.islower():
        lower_letters=lower_letters+1
name1=len(name)
print(upper_letters*100/name1,"Процент букв с верхним регистром")
print(lower_letters*100/name1,"Процент букв с нижним регистром")
# Получилось так
#Введите пожалуйста текст АААААааааа
#50.0 Процент букв с верхним регистром
#50.0 Процент букв с нижним регистром


