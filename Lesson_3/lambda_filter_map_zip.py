# def f(x):
#     x**2

# g = f
# print(f(1))
# print(g(1)) # работает одинаково


def f(x):
    return x**2


g = f # в переменную можно положить функцию

print(type(f))
print(type(g))

print(g(4))
print(f(4))



def calc1 (x):
    return x+10
# print(calc1(10))

def calc2(x):
    return x*10
# print(calc2(10))

def math(op, x):
    print(op(x))

math(calc2, 10)
math(calc1, 10)


def sum(x, y):
    return x+y

def mult(x, y):
    return x*y

def calc(op, a, b): # op  - отдельная функция
