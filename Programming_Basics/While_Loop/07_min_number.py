from sys import maxsize
min_number = maxsize

while True:
    data = input()

    if data == 'Stop':
        break

    else:
        current_number = int(data)
        if current_number < min_number:
            min_number = current_number
print(min_number)
