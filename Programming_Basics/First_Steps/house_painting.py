x = float(input())
y = float(input())
h = float(input())

front_wall_area = x * x - 1.2 * 2
back_wall_area = x * x
side_wall_area = x * y - 1.5 * 1.5
side_roof_area = x * y
front_roof_area = x * h / 2

green_paint = (front_wall_area + back_wall_area + 2 * side_wall_area) / 3.4
red_paint = (2 * side_roof_area + 2 * front_roof_area) / 4.3

print("{:.2f}".format(green_paint))
print("{:.2f}".format(red_paint))



