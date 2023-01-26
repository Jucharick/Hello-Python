# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.


data = [x for x in range(10)]

res = list(filter(lambda x: not x%2, data)) # x%2==0 тоже самое что x%2  / filter() - проверяет условие
print(res)