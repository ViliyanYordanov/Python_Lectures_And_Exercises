stadium_capacity = int(input())
total_fans = int(input())

team_1_fans_A = 0
team_1_fans_B = 0
team_2_fans_V = 0
team_2_fans_G = 0

for _ in range(total_fans):
    fan = input()
    if fan == 'A':
        team_1_fans_A += 1
    elif fan == 'B':
        team_1_fans_B += 1
    elif fan == 'V':
        team_2_fans_V += 1
    elif fan == 'G':
        team_2_fans_G += 1

print(f'{team_1_fans_A / total_fans * 100:.2f}%')
print(f'{team_1_fans_B / total_fans * 100:.2f}%')
print(f'{team_2_fans_V / total_fans * 100:.2f}%')
print(f'{team_2_fans_G / total_fans * 100:.2f}%')
print(f'{total_fans / stadium_capacity * 100:.2f}%')
