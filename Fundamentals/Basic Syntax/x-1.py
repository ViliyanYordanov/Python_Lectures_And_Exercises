quantity_of_decorations = int(input())
days_left_until_christmas = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

ornament_set_points = 5
tree_skirt_points = 3
tree_garland_points = 10
tree_lights_points = 17

cost = 0
spirit = 0

for current_day in range(1, days_left_until_christmas + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        cost += quantity_of_decorations * ornament_set_price
        spirit += ornament_set_points
    if current_day % 3 == 0:
        cost += quantity_of_decorations * tree_skirt_price + quantity_of_decorations * tree_garland_price
        spirit += tree_skirt_points + tree_garland_points
    if current_day % 5 == 0:
        cost += quantity_of_decorations * tree_lights_price
        spirit += tree_lights_points
        if current_day % 3 == 0:
            spirit += 30
    if current_day % 10 == 0:
        spirit -= 20
        cost += tree_lights_price + tree_garland_price + tree_skirt_price

if days_left_until_christmas % 10 == 0:
    spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")