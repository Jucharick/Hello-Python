# Это фрагмент программы, используемый
# многократно
# def function_name(x):
    # # body line 1
    # # . . .
    # # body line n
    # # optional return


# import f # путь к файлу f.py

# print(f.f(1))


def new_string(symbol, count = 3):
    return symbol * count
print(new_string('!', 5)) # !!!!!
print(new_string('!')) # !!!
print(new_string(4)) # 12


def concatenatio(*params): # неограниченное количество аргументов функции (перед аргументом ставим *)
    res: str = ""  # тип данных
    for item in params:
        res += item
    return res
print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError: ...  логика работы со строкой, не с числами 