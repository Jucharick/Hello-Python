# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.

li = [x for x in range(1, 20)]

li = list(map(lambda x: x+10,  li)) # каждое число списка увеличивается на 10

print(li)


data = list(map(int, input().split())) # map применяет функцию int (преобразует в число) каждый принимаемый input() элемент
print(data)

for e in data:
    print(e)

print('-----')

for e in data:
    print(e)