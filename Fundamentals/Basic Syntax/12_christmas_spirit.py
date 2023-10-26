quantity_of_decorations = int(input())
days_until_Christmas = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

points = 0
total_cost = 0

for current_day in range(1, days_until_Christmas + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2

    if current_day % 2 == 0:
        total_cost += ornament_set_price * quantity_of_decorations
        points += 5
    if current_day % 3 == 0:
        total_cost += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
        points += 13
    if current_day % 5 == 0:
        total_cost += tree_lights_price * quantity_of_decorations
        points += 17
        if current_day % 3 == 0:
            points += 30

    if current_day % 10 == 0:
        points -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price


if days_until_Christmas % 10 == 0:
    points -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {points}")