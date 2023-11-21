sequence_of_numbers = input().split()
data = input()
index_list = []
message = ''
len_data = len(data)


for number in sequence_of_numbers:
    current_sum = 0
    for x in number:
        current_sum += int(x)
    index_list.append(current_sum)

for value in index_list:
    current_index = 0
    for index in range(0, value):
        if current_index == len_data:
            current_index = 0
        current_index += 1
    message += data[current_index]
    data = data[:current_index - 1] + data[current_index:]
print(message)
