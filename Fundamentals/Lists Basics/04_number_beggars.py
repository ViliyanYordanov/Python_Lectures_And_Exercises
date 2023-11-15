string_of_integers = input().split(', ')
beggars = int(input())

final_list = []
beggar_amount = 0

for current_beggar in range(beggars):
    beggar_coins = 0
    for current_amount in range(current_beggar, len(string_of_integers), beggars):
        beggar_coins += int(string_of_integers[current_amount])
    final_list.append(beggar_coins)

print(final_list)
