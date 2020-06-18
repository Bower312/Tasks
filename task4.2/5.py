# def make_car(**kwargs):  #Перебор kwargs 
#     print(kwargs)
#     for i in kwargs.values():
#         print(i)
#     for x in kwargs.keys():
#         print(x)


# make_car(subaru = "outback", color="blue", tow_package="True")

# 5)Автомобили: напишите функцию для сохранения информации об
# автомобиле в словаре. Функция всегда должна возвращать
# производителя и название модели, но при этом она
# может получать произвольное количество именованных аргументов.
# Вызовите функцию с передачей обязательной информации и еще двух
# пар «имя—значение» (например, цвет и комплектация).
# Ваша функция должна работать для вызовов следующего вида:
# car = make_car(‘subaru’, ‘outback’, color=’blue’, tow_package=True)
# Выведите возвращаемый словарь и убедитесь в том, что вся
# информация была сохранена правильно.

def make_car(**kwargs):  #Перебор kwargs 
    for i,x in kwargs.items():
        print(i+':',x)


make_car(subaru = "outback", color="blue", tow_package="True")