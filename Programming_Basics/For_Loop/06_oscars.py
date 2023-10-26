actor_name = input()
academy_points = float(input())
number_of_judges = int(input())
all_points = academy_points

for _ in range(number_of_judges):
    name_judge = input()
    points_of_judge = float(input())

    all_points += len(name_judge) * points_of_judge / 2

    if all_points > 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {all_points:.1f}!')
        break
else:
    print(f"Sorry, {actor_name} you need {(1250.5 - all_points):.1f} more!")
