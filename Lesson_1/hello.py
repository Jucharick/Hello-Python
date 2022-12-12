print('Hello Python')


# типы данных и переменные 

a = 123
b = 1.223
value = None # в Python нельзя обозначить переменную, а значение для нее присвоить где-то ниже; для пустой переменной указывают тип None
# print(type(value))
# print(type(a))
# print(type(b))
value = 12345
# print(type(value))

s = 'hello Python'
# print(s)
st = 'hello \nworld' # \n - переход на новую строку
# print(st)

print(a, '-', b, '-', s)
print('{} - {} - {}'.format(a, b, s))
print(f'{a} - {b} - {s}') # интерполяция, данный способ вывода появился недавно

print('{1} - {2} - {0}'.format(a, b, s)) # меняем переменные местами

f = True
print(f)

list = [1,2,3,4,5,6, 'hello', 1.23]
print (list)