from sys import maxsize

num = int(input())
max_num = -maxsize
numbers_sum = 0

for i in range(0, num):
    n = int(input())
    numbers_sum += n
    if n > max_num:
        max_num = n
if numbers_sum - max_num == max_num:
    print("Yes")
    print(f'Sum = {max_num}')
else:
    print("No")
    print(f'Diff = {abs(max_num - (numbers_sum - max_num))}')