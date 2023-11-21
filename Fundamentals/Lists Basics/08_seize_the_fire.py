fire_data = input().split('#')
water_amount = int(input())
effort = 0
total_fire = 0
cells_list = []

for current_fire in range(len(fire_data)):
    if water_amount <= 0:
        break
    current_fire_list = fire_data[current_fire].split(' = ')

    if current_fire_list[0] == 'High' and 80 < int(current_fire_list[1]) < 126:
        if int(current_fire_list[1]) > water_amount:
            continue
        water_amount -= int(current_fire_list[1])
        effort += int(current_fire_list[1]) * 0.25
        total_fire += int(current_fire_list[1])
        cells_list.append(current_fire_list[1])
    elif current_fire_list[0] == 'Medium' and 50 < int(current_fire_list[1]) < 81:
        if int(current_fire_list[1]) > water_amount:
            continue
        water_amount -= int(current_fire_list[1])
        effort += int(current_fire_list[1]) * 0.25
        total_fire += int(current_fire_list[1])
        cells_list.append(current_fire_list[1])
    elif current_fire_list[0] == 'Low' and 0 < int(current_fire_list[1]) < 51:
        if int(current_fire_list[1]) > water_amount:
            continue
        water_amount -= int(current_fire_list[1])
        effort += int(current_fire_list[1]) * 0.25
        total_fire += int(current_fire_list[1])
        cells_list.append(current_fire_list[1])

joined_list = '\n - '.join(cells_list)
print(f'Cells:\n - {joined_list}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')