first_string = input()
second_string = input()
last_string = first_string

for i in range(len(first_string)):
    current_string = second_string[:i + 1] + first_string[i + 1:]

    if current_string != last_string:
        print(current_string)
        last_string = current_string
