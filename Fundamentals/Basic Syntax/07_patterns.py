n = int(input())

for i in range(1, n + 1):
    for j in range(0, i):
        print('*', end='')
    print()
for a in range(n - 1, 0, -1):
    for b in range(a, 0, -1):
        print('*', end='')
    print()