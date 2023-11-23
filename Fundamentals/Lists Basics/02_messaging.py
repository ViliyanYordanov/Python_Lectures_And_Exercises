# sequence_of_numbers = input().split()
# data = input()
# index_list = []
# message = ''
# len_data = len(data)
#
#
# for number in sequence_of_numbers:
#     current_sum = 0
#     for x in number:
#         current_sum += int(x)
#     index_list.append(current_sum)
#
# for value in index_list:
#     current_index = 0
#     for index in range(0, value):
#         if current_index == len_data:
#             current_index = 0
#         current_index += 1
#     message += data[current_index]
#     data = data[:current_index - 1] + data[current_index:]
# print(message)


some_sequence = input().split()
some_string = input()

list_of_some_string = list(some_string)
message = []

for index in range(len(some_sequence)):
    index_as_int = int(some_sequence[index])
    index_as_list = list(map(int, str(index_as_int)))
    current_sum = sum(index_as_list)

    if current_sum < len(list_of_some_string):
        message.append(list_of_some_string[current_sum])
        list_of_some_string.pop(current_sum)
    else:
        message.append(list_of_some_string[current_sum - len(list_of_some_string)])
        list_of_some_string.pop(current_sum - len(list_of_some_string))

print(''.join(message))