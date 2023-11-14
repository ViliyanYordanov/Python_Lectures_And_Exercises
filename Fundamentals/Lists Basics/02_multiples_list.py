factor = int(input())
count = int(input())
data_list = []
for x in range (count):
    data_list.append(count * factor)
    count -= 1
data_list.reverse()
print(data_list)

