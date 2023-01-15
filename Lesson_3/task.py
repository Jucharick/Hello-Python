# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]


path = '/Users/Юлия Чарикова/Desktop/GeekBrains/I четверть - блок 2/Знакомство с языком Python/HelloPython/Lesson_3/file_task.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '': # пока строка не пустая
    space_pos = data.index(' ') # найти первую позицию пробела
    numbers.append(int(data[:space_pos])) # взять все, что находится от первого символа до позиции этого пробела / превратить в число / добавить в список numbers
    data = data[space_pos+1:] # обновить строку с учетом того что с учетом обработанного нам больше не нужно использовать

out = []
for e in numbers:
    if not e % 2:
        out.append((e,e **2))
print(out)


# lambda

def select(f, col):
    return [f(x) for x in col]
def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()
data = select(int, data)
data = where(lambda e: not e % 2, data)
data = list(select(lambda e: (e, e**2), data))


# map() and filter()

data = '1 2 3 5 8 15 23 38'.split()
data = list(map(int, data))
data = list(filter(lambda e: not e % 2, data))
data = list(map(lambda e: (e, e**2), data))
print(data)