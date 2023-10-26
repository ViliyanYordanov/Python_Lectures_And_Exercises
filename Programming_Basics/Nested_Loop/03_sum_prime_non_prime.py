number = input()
prime_numbers_sum = 0
non_prime_numbers_sum = 0

while number != 'stop':
    current_number = int(number)
    if current_number < 0:
        print('Number is negative.')
        number = input()
        continue
    counter = 0
    for i in range(1, current_number + 1):
        if current_number % i == 0:
            counter += 1
    if counter > 2:
        non_prime_numbers_sum += current_number
    else:
        prime_numbers_sum += current_number
    number = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")