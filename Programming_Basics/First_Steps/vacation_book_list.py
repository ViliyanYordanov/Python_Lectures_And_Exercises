import math

number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())

hours_per_day = number_of_pages/pages_per_hour/number_of_days

print(math.floor(hours_per_day))
