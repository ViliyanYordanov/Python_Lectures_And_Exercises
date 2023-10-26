first_num = int(input())
second_num = int(input())
third_num = int(input())

largest_num = 0

if first_num > second_num:
    largest_num = first_num
else:
    largest_num = second_num

if largest_num < third_num:
    largest_num = third_num

print(largest_num)