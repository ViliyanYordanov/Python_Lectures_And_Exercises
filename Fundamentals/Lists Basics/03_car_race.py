data = input().split()
middle_index = len(data) // 2
left_car_time = 0
right_car_time = 0

for current_time_left_car in range(0, middle_index):
    if data[current_time_left_car] == '0':
        left_car_time *= 0.8
    left_car_time += int(data[current_time_left_car])


for current_time_right_car in range(len(data) - 1, middle_index, - 1):
    if data[current_time_right_car] == '0':
        right_car_time *= 0.8
    right_car_time += int(data[current_time_right_car])

winner = ''
first_place_time = 0

if left_car_time < right_car_time:
    winner = 'left'
    first_place_time = left_car_time
else:
    winner = 'right'
    first_place_time = right_car_time
print(f"The winner is {winner} with total time: {first_place_time:.1f}")
