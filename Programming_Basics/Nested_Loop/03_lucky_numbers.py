n = int(input())
if 1 < n < 10000:
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                for d in range(1, n):
                    if a + b == c + d and n % (a + b) == 0 and n % (c + d) == 0:
                        number = str(a) + str(b) + str(c) + str(d)
                        if 0 < int(number) < 10000:
                            print(f'{a}{b}{c}{d}', end=' ')
