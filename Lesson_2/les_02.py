# with open('file.txt', 'a') as data:
#     data.write('line aaaaa1\n')
#     data.write('line aaaaa2\n')

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close()

# exit() # функция позволяет не выполнять код, написанный после
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()