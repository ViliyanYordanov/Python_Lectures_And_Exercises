n = int(input())
previous_sum = 0
max_diff = 0

for _ in range(n):
    number_1 = int(input())
    number_2 = int(input())

    current_sum = number_1 + number_2

    if previous_sum == 0:
        previous_sum = current_sum

    if current_sum != previous_sum:
        diff = abs(current_sum - previous_sum)

        if diff > max_diff:
           max_diff = diff

    previous_sum = current_sum

if max_diff == 0:
    print(f"Yes, value={previous_sum}" )
else:
    print(f"No, maxdiff={max_diff}")

