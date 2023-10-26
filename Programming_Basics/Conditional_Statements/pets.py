from math import floor
from math import ceil

days = int(input())
food_kg = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_g = float(input())

dog_food = dog_food_per_day_kg * days
cat_food = cat_food_per_day_kg * days
turtle_food = turtle_food_per_day_g / 1000 * days

needed_food = dog_food + cat_food + turtle_food

if food_kg >= needed_food:
    print(f"{floor(food_kg - needed_food)} kilos of food left.")
else:
    print(f'{ceil(needed_food - food_kg)} more kilos of food are needed.')

