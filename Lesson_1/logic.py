# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |,^
# is, is not, in, not in
# gen

a = 1 < 4 < 5 < 10 # можно использовать не только двойные неравенства
print (a)

b = [1, 2]
c = [1, 2]
print (b==c)

d = 'qwe'
e = 'qwe'
print (d==e)

func = 1
T = 4
x = 123
print(func<T>(x))

f =  1 > 2 or 4 < 6
print(f)

g = [1,2,3,4]

print(g)
print(2 in g)
print(not 2 in g)

# is_odd = g[0] % 2 == 0
is_odd = not g[0] % 2
print(is_odd)