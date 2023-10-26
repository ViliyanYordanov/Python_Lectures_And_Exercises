n = int(input())
total_sum = 0
counter = 0

for _ in range(n):
    number = int(input())
    total_sum += number
    counter += 1

average = total_sum / counter

print(f'{average:.2f}')
