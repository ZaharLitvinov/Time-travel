import random
for i in ['?', '?', '?', '?', '?', ' ', '?', '?', '?', '?', '?', '?', '?']:
    if i == '?':
        n = random.randint(0, 9)
        print(n, sep='', end='')
    else:
        print(' ', sep='', end='')