from math import floor

tournament_participated = int(input())
starting_points = int(input())
points = 0
tournaments_won = 0
for _ in range(tournament_participated):
    current_tournament_place = input()

    if current_tournament_place == 'W':
        points += 2000
        tournaments_won += 1
    elif current_tournament_place == 'F':
        points += 1200
    elif current_tournament_place == 'SF':
        points += 720
all_points = starting_points + points

print(f"Final points: {all_points}")
print(f"Average points: {floor(points / tournament_participated)}")
print(f'{(tournaments_won / tournament_participated * 100):.2f}%')