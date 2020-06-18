numbers=[]
for value in range(1,1000000+1):
    number=value
    numbers.append(number)
    print(value)
print("Минимальная сумма " , min(numbers))
print("Максимальная сумма " , max(numbers))
print("Сумма " , sum(numbers))
