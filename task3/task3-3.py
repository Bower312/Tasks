#Школа решила заменить парты в 3 классах. На каждой парте сидят по 2 человека.
#Учитываю количество чел. в каждом классе-выведите наименьшее возможное количество столов.

room1=int(input("Введите количество учеников в 1 классе "))
room2=int(input("Введите количество учеников в 2 классе "))
room3=int(input("Введите количество учеников в 3 классе "))
a=room1/2
b=room2/2
c=room3/2
import math
a=int(math.ceil(a)) #вписал в каждую строку чтобы округляла в большую сторону.
b=int(math.ceil(b))
c=int(math.ceil(c))
# okrug=sum.round() через раунд не получилось.
sum=a+b+c
print("нужно закупить",sum,"столов")
