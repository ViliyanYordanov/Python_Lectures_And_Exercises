from math import sqrt
from math import floor


def closest_point(x1, y1, x2, y2):
    z1 = sqrt((x1 ** 2) + (y1 ** 2))
    z2 = sqrt((x2 ** 2) + (y2 ** 2))

    if z1 < z2:
        print(f"({floor(x1)}, {floor(y1)})")
    elif z1 > z2:
        print(f"({floor(x2)}, {floor(y2)})")
    else:
        print(f"({floor(x1)}, {floor(y1)})")


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
closest_point(x_1, y_1, x_2, y_2)
