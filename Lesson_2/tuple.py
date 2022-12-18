t = ()
print(type(t)) # tuple
t = (1,)
print(type(t)) # tuple
t = (1)
print(type(t)) # int
t = (28, 9, 1990)
print(type(t)) # tuple
colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue']
t = tuple(colors)
print(t) # ('red', 'green', 'blue')



a, b = 3, 4
print(a, b)

c = (3, 4, 4, 6, 7)
print(c)
print(c[0])
print(c[-1]) # последний элемент
print(c[-2]) # предпоследний элемент
# для картежей не работает присваивание с[0] = 12 => именно поэтому кортеж определяют как неизменяемый список



t1 = tuple(['red', 'green', 'blue']) # список [] преобразовываем в кортеж ()
red, green, blue = t1 # кортеж () преобразовываем в переменные
print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue