name=input("введите слова через пробел? ")
name=name.split(" ")
name.sort(key=len)
print(name)
#ответ получился такой
#['son', 'kraska', 'mashina', 'devochka']