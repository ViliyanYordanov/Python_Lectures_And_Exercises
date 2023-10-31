number = int(input())

for digits in range(1, number + 1):
    counter = 0
    for x in range(len(str(digits))):
        number_as_string = str(digits)
        counter += int(number_as_string[x])

    if counter == 5 or counter == 7 or counter == 11:
        print(f'{digits} -> True')
    else:
        print(f'{digits} -> False')
