n = int(input())
previous_numbers = 0
max_diff = 0

for _ in range(n):
    number_1 = int(input())
    number_2 = int(input())

    current_numbers = number_1 + number_2
    if previous_numbers == 0:
        pass
    elif current_numbers != previous_numbers:
        diff = abs(previous_numbers - current_numbers)

        if diff > max_diff:
            max_diff = diff

    previous_numbers = current_numbers

if max_diff == 0:
    print(f"Yes, value={previous_numbers}")
else:
    print(f"No, maxdiff={max_diff}")
