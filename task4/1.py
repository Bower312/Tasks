## 1) Написать функцию season, принимающую 1 аргумент — номер месяца
# (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима,
# весна, лето или осень).
season=int(input("Укажите месяц: "))
zima=range(1,3)
vesna=range(3,6)
leto=range(6,9)
osen=range(9,12)
if season <3:
    print("зима")
elif season <6 and season >1:
    print("Весна")
elif season <9 and season >1:
    print("Лето")
elif season <12 and season >1:
    print("Осень")
elif season <13:
    print("Зима")
else:
    print("Нет такого месяца))))")


