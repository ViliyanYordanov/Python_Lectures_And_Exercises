first_number = int(input())
second_number = int(input())
print('Before:')
print(f'a = {first_number}')
print(f'b = {second_number}')
exchange_variable = first_number
first_number = second_number
print('After:')
print(f'a = {first_number}')
print(f'b = {exchange_variable}')