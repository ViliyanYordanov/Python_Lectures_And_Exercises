points = int(input())
bonus_points = 0

if points <= 100:
    bonus_points = 5
elif 100 < points < 1000:
    bonus_points = points * 20 / 100
elif points > 1000:
    bonus_points = points * 10 / 100

if points % 2 ==0:
    bonus_points = bonus_points + 1
if points % 10 == 5:
    bonus_points = bonus_points + 2

print(bonus_points)
print(bonus_points + points)
