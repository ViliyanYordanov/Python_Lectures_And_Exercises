n = int(input())
counter = 0

for x in range(0, n + 1):
    for y in range (0, n + 1):
        for z in range(0, n + 1):
            result = x + y + z
            if result == n:
                counter += 1
print(counter)