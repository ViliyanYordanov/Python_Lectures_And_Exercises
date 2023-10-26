amount_to_be_collected = int(input())
counter = 0
total_amount = 0
cash = 0
cash_counter = 0
card = 0
card_counter = 0

while total_amount < amount_to_be_collected:
    data = input()
    if data == 'End':
        break
    current_amount = int(data)
    counter += 1

    if counter % 2 != 0:
        if current_amount > 100:
            print("Error in transaction!")

        else:
            print("Product sold!")
            total_amount += current_amount
            cash += current_amount
            cash_counter += 1

    elif counter % 2 == 0:
        if current_amount < 10:
            print("Error in transaction!")

        else:
            print("Product sold!")
            total_amount += current_amount
            card += current_amount
            card_counter += 1

average_cs = cash / cash_counter
average_cc = card / card_counter

if total_amount >= amount_to_be_collected:
    print(f"Average CS: {average_cs:.2f}")
    print(f"Average CC: {average_cc:.2f}")
else:
    print("Failed to collect required money for charity.")
