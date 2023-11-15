received_gifts = input().split()

while True:
    command = input()
    if command == 'No Money':
        break
    list_of_command = command.split()

    if list_of_command[0] == 'OutOfStock':
        for current_gift in range(len(received_gifts)):
            if received_gifts[current_gift] == list_of_command[1]:
                received_gifts[current_gift] = 'None'

    elif list_of_command[0] == 'Required':
        if int(list_of_command[2]) < len(received_gifts):
            index_of_command = int(list_of_command[2])
            received_gifts[index_of_command] = list_of_command[1]

    elif list_of_command[0] == 'JustInCase':
        received_gifts[len(received_gifts) - 1] = list_of_command[1]

final_list = []
for food in range(len(received_gifts)):
    if received_gifts[food] != 'None':
        final_list.append(received_gifts[food])

final_list = ' '.join(final_list)
print(final_list)
