deck_of_cards = input().split()
number_of_shuffles = int(input())

for current_shuffle in range(number_of_shuffles):
    middle_of_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_deck]
    right_part = deck_of_cards[middle_of_deck:]
    final_deck = []
    for card in range(len(left_part)):
        final_deck.append(left_part[card])
        final_deck.append(right_part[card])
    deck_of_cards = final_deck
print(final_deck)
