from math import floor
N = int(input())
points = 0
red_counter = 0
orange_counter = 0
yellow_counter = 0
white_counter = 0
black_counter = 0
other_color = 0

for i in range(1, N + 1):
    color = input()

    if color == 'red':
        points += 5
        red_counter += 1
    elif color == 'orange':
        points += 10
        orange_counter += 1
    elif color == 'yellow':
        points += 15
        yellow_counter += 1
    elif color == 'white':
        points += 20
        white_counter += 1
    elif color == 'black':
        points = floor(points / 2)
        black_counter += 1
    else:
        other_color += 1
        continue

print(f"Total points: {points}")
print(f"Red balls: {red_counter}")
print(f"Orange balls: {orange_counter}")
print(f"Yellow balls: {yellow_counter}")
print(f"White balls: {white_counter}")
print(f"Other colors picked: {other_color}")
print(f"Divides from black balls: {black_counter}")