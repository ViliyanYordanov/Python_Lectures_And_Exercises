numbers = int(input())

for _ in range(numbers):
    current_number = int(input())

    if current_number % 2 == 0:
        continue
    else:
        print(f'{current_number} is odd!')
        break
else:
    print('All numbers are even.')