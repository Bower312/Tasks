#2)Найти минимальное число которое отсуствует в данном нам списке и вывести на экран.

def list_min(list1):
    list3=[]
    list2=list(range(min(list1),max(list1)))
    print(list2)
    for i in list2:
        if i not in list1:
            list3.append(i)
    print(list3)   
    print(min(list3))
a=[9,7,16,40,36]

list_min(a)
        








