n = int(input())

sum_1 = 0
sum_2 = 0

for _ in range(n):
    current_number = int(input())
    sum_1 += current_number

for _ in range(n):
    current_number2 = int(input())
    sum_2 += current_number2

if sum_1 == sum_2:
    print(f'Yes, sum = {sum_1}')
else:
    print(f"No, diff = {abs(sum_1 - sum_2)}")
