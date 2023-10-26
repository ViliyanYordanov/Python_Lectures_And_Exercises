men = int(input())
women = int(input())
tables = int(input())

for m in range(1, men + 1):
    for j in range(1, women + 1):
        while tables > 0:
            print(f'({m} <-> {j})', end=' ')
            tables -= 1
            break