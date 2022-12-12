# Управляющие конструкции: if, if-else
# if condition:
#  # operator 1
#  # operator 2
#  # ...
#  # operator n
# else:
#  # operator n + 1
#  # operator n + 2
#  # ...
#  # operator n + m

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)


# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)


# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)


# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)


for i in 1, -2, 3, 14, 5:
    print(i**2)

print()
list = [1,2,3,4,5,6]
for i in list:
    print(i**2)

print()
r = range(10) # выдает значения от 0 до 9
for i in r:
    print(i)

print()
for i in range(1, 10, 2): # от 1 до 9 с приращением 2 (шагом)
    print(i)

print()
for j in 'qwerty':
    print(j)