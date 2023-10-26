M = int(input())
counter = 0
flag = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == M and a < b and c > d:
                    print(f'{a}{b}{c}{d} ',end='')
                    counter += 1
                    if counter == 4:
                        password = str(a) + str(b) + str(c) + str(d)
                        flag = True
if flag:
    print()
    print(f'Password: {int(password)}')
else:
    print()
    print('No!')
