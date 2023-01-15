list = []

# for i in range(1, 21):
#       if(i%2 == 0):
#           list.append(i)
# print(list)

list = [i for i in range(1, 21) if(i%2 == 0)] # второй тип записи добавления элементов в список list
print(list)

list1 = [(i, i) for i in range(1, 21) if(i%2 == 0)] 
print(list1)

def f(x):
    return x**3

list2 = [(i, f(i)) for i in range(1, 21) if(i%2 == 0)] 
print(list2)