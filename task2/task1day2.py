#Задача пусть USER ведет час мин и секунду. Ваша задача найти разницу между отрезками времени и предоставить это всё в секундах.

utro=int(input("В какой час вы приходите на работу?   "))
min=int(input("мин "))
sek=int(input("сек "))
vecher=int(input("а во сколько вы уходите? "))
min2=int(input("мин "))
sek2=int(input("сек "))

print(str(utro)+":"+str(min)+":"+str(sek))
print(str(vecher)+":"+str(min2)+":"+str(sek2))
x=(utro*60*60)+(min*60)+sek
y=(vecher*60*60)+(min2*60)+sek2 #
print(y-x)