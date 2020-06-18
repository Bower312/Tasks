#напишите программу , которая принимает два списка и выводит все элементы первого, которых нет во втором.

spisoks=["1", "2", "3", "4", "5","6", "7"] # 
tables=["1", "2", "3", "4", "5"]
newlist=[]
for spisok in spisoks:
    if spisok not in tables:
        newlist.append(spisok)
print(newlist)
    

