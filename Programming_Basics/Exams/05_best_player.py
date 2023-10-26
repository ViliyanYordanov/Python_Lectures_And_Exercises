name = input()
best_player = ''
top_goals = 0
hat_trick = False

while name != 'END':
    goals = int(input())
    if goals > top_goals:
        top_goals = goals
        best_player = name

    if top_goals >= 3:
        hat_trick = True
    if goals >= 10:
        break
    name = input()

print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {top_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {top_goals} goals.")