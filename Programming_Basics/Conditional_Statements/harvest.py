from math import floor
from math import ceil

x_square_m = int(input())
y_grape_per_square_m = float(input())
z_wine_litres_for_sale = int(input())
workers = int(input())

total_grape = x_square_m * y_grape_per_square_m
wine = total_grape * 0.40 / 2.5

if wine < z_wine_litres_for_sale:
    print(f'It will be a tough winter! More {floor(z_wine_litres_for_sale - wine)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {ceil(wine)} liters.')
    print(f'{ceil(wine - z_wine_litres_for_sale)} liters left -> {ceil((wine - z_wine_litres_for_sale) / workers)} '
          f'liters per person.')
