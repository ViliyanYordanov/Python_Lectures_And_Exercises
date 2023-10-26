count_cargo = int(input())
bus = 0
truck = 0
train = 0
total_weight = 0
bus_weight = 0
truck_weight = 0
train_weight = 0
for _ in range(count_cargo):
    current_weight = int(input())
    total_weight += current_weight

    if current_weight <= 3:
        bus += 200 * current_weight
        bus_weight += current_weight
    elif 3 < current_weight <= 11:
        truck += 175 * current_weight
        truck_weight += current_weight
    elif 11 < current_weight:
        train += 120 * current_weight
        train_weight += current_weight
total_price = bus + truck + train
print(f'{total_price / total_weight:.2f}')
print(f'{bus_weight / total_weight * 100:.2f}%')
print(f'{truck_weight / total_weight * 100:.2f}%')
print(f'{train_weight / total_weight * 100:.2f}%')