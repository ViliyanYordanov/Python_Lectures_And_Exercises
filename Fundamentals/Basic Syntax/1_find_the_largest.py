# number = int(input())
# new_number = ''
#
# l = [int(x) for x in str(number)]
#
# l.sort(reverse=True)
# for x in l:
#     new_number += str(x)
# print(new_number)

# num = input("Enter a number: ")
#
# # Convert the number into a list of its digits
# digits = [int(digit) for digit in num]
#
# # Sort the digits in descending order
# sorted_digits = sorted(digits, reverse=True)
#
# # Join the sorted digits to create the largest number
# largest_number = ''.join(map(str, sorted_digits))
#
# # Print the largest number
# print("The largest number that can be formed is:", largest_number)

first_number = int(input())

listed = [int(x) for x in str(first_number)]

listed.sort(reverse=True)

second_number = ''.join(str(listed))

print(str(second_number))