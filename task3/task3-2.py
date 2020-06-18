bazar=int(input("Введите количество яблок "))
chel=int(input("Количество человек "))

a=bazar//chel
b=bazar-(a*chel)
print("каждый получит по", a,"остаток", b)