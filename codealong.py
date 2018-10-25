# lists

clothes = ['socks', 'belt', 'shirt']
# switch belt for necklace
clothes[1] = 'necklace'
# add new item
clothes.append('pants')


print(clothes)


# if else statement
if 'hat' in clothes:
    print('wearing a hat')

if clothes[0] == 'pants':
    print('pants are first')
else:
    print('pants are not first')

# loops

# for loops iterate over list
# while loops, loops while condition is true
for item in clothes:
    print(item)

while len(clothes) > 0:
    print(clothes[0])
    del clothes[0]