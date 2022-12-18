list1 = [1,2,3,4,5,6]
list2 = list1 # копируем список

for e in list1:
    print(e)

print()

for e in list2:
    print(e)

print()


list1[1] = 123 # изменяется и в пепвом и во втором списке при таком копировании list2 = list1 (аналогично и наоборот)

for e in list1:
    print(e)

print()

for e in list2:
    print(e)

print()
print(list1)
list1.pop() # удаляем последний элемент
print(list1)
print(len(list1)) # длина списка

list1.pop(2) # удаляем элемент с индексом [2]
print(list1)

list1.insert(2, 11) # добавляем в список элемент = 11 на позицию [2]
print(list1)

list1.append(111) # добавляем в конец списка
print(list1)