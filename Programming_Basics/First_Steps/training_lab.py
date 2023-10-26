w = float(input())
h = float(input())

width = h - 1
number_of_desks_per_row = width // 0.7
number_of_rows = w // 1.2

total_desks = number_of_desks_per_row * number_of_rows - 3
print("{:.0f}".format(total_desks))
