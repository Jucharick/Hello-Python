print("Введите a")
a = int(input())
print("Введите b")
b = int(input())

# print(a, b)
# print('{} - {}'.format(a, b))
# print(f'{a} - {b}')

print(a, " + ", b, " = ", a+b)   # выведет 1020, потому что по умолчанию input() работает со строками => добавим int() и преобразуем в число => 30