amount_to_be_collected = int(input())
counter = 0
cs_amount = 0
cs_counter = 0
cc_amount = 0
cc_counter = 0

while amount_to_be_collected > 0:
    data = input()
    if data != 'End':
        current_amount = int(data)
        counter += 1
        if counter % 2 != 0:
            if current_amount > 100:
                print("Error in transaction!")
            else:
                amount_to_be_collected -= current_amount
                print("Product sold!")
                cs_amount += current_amount
                cs_counter += 1
        else:
            if current_amount < 10:
                print("Error in transaction!")
            else:
                amount_to_be_collected -= current_amount
                print("Product sold!")
                cc_amount += current_amount
                cc_counter += 1
        if amount_to_be_collected <= 0:
            average_cs = cs_amount / cs_counter
            average_cc = cc_amount / cc_counter
            print(f"Average CS: {average_cs:.2f}")
            print(f"Average CC: {average_cc:.2f}")
    else:
        print("Failed to collect required money for charity.")
        break
