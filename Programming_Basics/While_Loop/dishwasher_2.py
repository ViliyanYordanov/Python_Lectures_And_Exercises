ml_per_bottle = 750
ml_for_plate = 5
ml_for_pot = 15
counter = 0
total_bottles = int(input())
total_ml = ml_per_bottle * total_bottles
clean_plates = 0
clean_pots = 0


while total_ml >= 0:
    data = input()
    if data != 'End':
        current_dishes = int(data)
        counter += 1
        if counter % 3 != 0:
            total_ml -= current_dishes * ml_for_plate
            clean_plates += current_dishes
        else:
            total_ml -= current_dishes * ml_for_pot
            clean_pots += current_dishes
    else:
        break
if total_ml >= 0:
    print("Detergent was enough!")
    print(f"{clean_plates} dishes and {clean_pots} pots were washed.")
    print(f"Leftover detergent {total_ml} ml.")
else:
    print(f"Not enough detergent, {abs(total_ml)} ml. more necessary!")