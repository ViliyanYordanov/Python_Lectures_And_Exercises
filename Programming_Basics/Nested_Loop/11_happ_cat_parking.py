days = int(input())
hours = int(input())
total = 0
total_sum = 0
for d in range(1, days + 1):
    for h in range(1, hours + 1):
        if d % 2 == 0 and h % 2 != 0:
            total += 2.50
        elif d % 2 != 0 and h % 2 == 0:
            total += 1.25
        else:
            total += 1
    print(f"Day: {d} - {total:.2f} leva")
    total_sum += total
    total = 0
print(f"Total: {total_sum:.2f} leva")
