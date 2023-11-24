data = input().split()

absolute_list = []

for number in data:
    absolute_list.append(abs(float(number)))

print(absolute_list)