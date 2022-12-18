dictionary = {}
dictionary = \
            {
            'up': '↑',
            'left': '←',
            'down': '↓',
            'right': '→'
            }
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться

for k in dictionary.keys():
    print(k)

for v in dictionary.values():
    print(v)

for i in dictionary.items():
    print(i)