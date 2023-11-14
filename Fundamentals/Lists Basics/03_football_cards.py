team_a_cards = []
team_b_cards = []

data = input()
split_data = data.split(' ')
for current_player in range(len(split_data)):
    new_data = split_data[current_player].split('-')
    if new_data[0] == 'A':
        team_a_cards.append('-'.join(new_data))
    elif new_data[0] == 'B':
        team_b_cards.append('-'.join(new_data))
team_a_red_cards = len(set(team_a_cards))
team_b_red_cards = len(set(team_b_cards))

    if 11 - team_a_red_cards < 7 or 11 - team_b_red_cards < 7:
        print(f"Team A - {11 - team_a_red_cards}; Team B - {11 - team_b_red_cards}")
        print("Game was terminated")
    else:
        print(f"Team A - {11 - team_a_red_cards}; Team B - {11 - team_b_red_cards}")
    