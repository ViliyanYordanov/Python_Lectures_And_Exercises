# team_a_cards = []
# team_b_cards = []
#
# data = input()
# split_data = data.split(' ')
# for current_player in range(len(split_data)):
#     new_data = split_data[current_player].split('-')
#     if new_data[0] == 'A':
#         team_a_cards.append('-'.join(new_data))
#     elif new_data[0] == 'B':
#         team_b_cards.append('-'.join(new_data))
# team_a_red_cards = len(set(team_a_cards))
# team_b_red_cards = len(set(team_b_cards))
#
#     if 11 - team_a_red_cards < 7 or 11 - team_b_red_cards < 7:
#         print(f"Team A - {11 - team_a_red_cards}; Team B - {11 - team_b_red_cards}")
#         print("Game was terminated")
#     else:
#         print(f"Team A - {11 - team_a_red_cards}; Team B - {11 - team_b_red_cards}")
#

team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

data = input().split()

for current_player in range(len(data)):
    if data[current_player] in team_a:
        team_a.remove(data[current_player])
    elif data[current_player] in team_b:
        team_b.remove(data[current_player])
    if len(team_a) < 7 or len(team_b) < 7:
        print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
        print("Game was terminated")
        break
else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")