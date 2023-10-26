goal = 10000
total_steps = 0
data = input()

while data != 'Going home':
    current_steps = int(data)
    total_steps += current_steps

    if total_steps >= goal:
        print("Goal reached! Good job!")
        print(f'{total_steps - goal} steps over the goal! ')
        break
    data = input()
else:
    data = input()
    current_steps = int(data)
    total_steps += current_steps

    if total_steps >= goal:
        print("Goal reached! Good job!")
        print(f'{total_steps - goal} steps over the goal! ')

    else:
        print(f"{goal - total_steps} more steps to reach goal.")
