length = int(input())
width = int(input())
height = int(input())
percentage = float(input()) / 100

area = length * width * height
area_litres = area / 1000
used_space = percentage * area_litres

water_space = area_litres - used_space

print(water_space)
