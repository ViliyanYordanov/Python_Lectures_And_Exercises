animals_string = input()
split_animal_string = animals_string.split(', ')

for current_animal in range(len(split_animal_string) -1, -1, -1):
    if split_animal_string[-1] == 'wolf':
        print('Please go away and stop eating my sheep')
        break
    elif split_animal_string[current_animal] == 'wolf':
        print(f'Oi! Sheep number {len(split_animal_string) - 1 - current_animal}! You are about to be eaten by a wolf!')
        break

