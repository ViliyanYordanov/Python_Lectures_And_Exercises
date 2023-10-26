num = int(input())

cycle_1 = 0
cycle_2 = 0
cycle_3 = 0
cycle_4 = 0
cycle_5 = 0

for _ in range(num):
    n = int(input())

    if 0 < n < 200:
        cycle_1 += 1

    elif 200 <= n < 400:
        cycle_2 += 1

    elif 400 <= n < 600:
        cycle_3 += 1

    elif 600 <= n < 800:
        cycle_4 += 1

    elif 800 <= n <= 1000:
        cycle_5 += 1

p1 = cycle_1 / num * 100
p2 = cycle_2 / num * 100
p3 = cycle_3 / num * 100
p4 = cycle_4 / num * 100
p5 = cycle_5 / num * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')