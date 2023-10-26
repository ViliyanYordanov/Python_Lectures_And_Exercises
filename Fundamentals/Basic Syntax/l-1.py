n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print('* ', end='')
    print()
for m in range(n -1, -1, -1):
    for n in range(m):
        print('* ', end='')
    print()