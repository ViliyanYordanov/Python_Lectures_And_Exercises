n = int(input())
even_list = []
odd_list = []
positive_list = []
negative_list = []
for _ in range(n):
    current_number = int(input())

    if current_number % 2 == 0:
        even_list.append(current_number)
    if current_number % 2 != 0:
        odd_list.append(current_number)
    if current_number >= 0:
        positive_list.append(current_number)
    if current_number < 0:
        negative_list.append(current_number)
command = input()
command_list = []
if command == 'even':
    command_list = even_list
elif command == 'odd':
    command_list = odd_list
elif command == 'positive':
    command_list = positive_list
else:
    command_list = negative_list
print(command_list)
