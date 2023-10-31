# year = int(input())
# special_year = False
# while not special_year:
#     year += 1
#     year_as_string = str(year)
#     special_year = True
#     for digit in year_as_string:
#         if year_as_string.count(digit) != 1:
#             special_year = False
#             break
# print(year)


# year = int(input())
# while True:
#     year += 1
#     year_as_string = str(year)
#     if len(set(year_as_string)) == len(year_as_string):
#         print(year)
#         break

year = int(input())
while True:
    year += 1
    counter = 1
    year_as_string = str(year)
    for index, digit in enumerate(year_as_string):
        for control_index in range(index + 1, len(year_as_string)):
            if year_as_string[control_index] == digit:
                counter += 1
        if counter > 1:
            break
    if counter == 1:
        break
print(year)