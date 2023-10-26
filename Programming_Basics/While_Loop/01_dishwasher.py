detergent_bottles = int(input())

total_ml = detergent_bottles * 750
plates_ml = 5
plates_counter = 0
pots_ml = 15
pots_counter = 0
counter = 0
vessels_ml = 0

while vessels_ml < total_ml:
    data = input()
    if data == 'End':
        break

    current_vessels = int(data)
    counter += 1

    if counter % 3 == 0:
        vessels_ml = vessels_ml + current_vessels * pots_ml
        pots_counter += current_vessels
    else:
        vessels_ml = vessels_ml + current_vessels * plates_ml
        plates_counter += current_vessels
    if vessels_ml > total_ml:
        break

if total_ml >= vessels_ml:
    print("Detergent was enough!")
    print(f"{plates_counter} dishes and {pots_counter} pots were washed.")
    print(f"Leftover detergent {total_ml - vessels_ml} ml.")
else:
    print(f"Not enough detergent, {vessels_ml - total_ml} ml. more necessary!")
