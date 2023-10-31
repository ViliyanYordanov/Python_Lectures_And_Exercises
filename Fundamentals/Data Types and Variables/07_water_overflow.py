number_of_lines = int(input())
capacity = 255
poured_litres = 0
for _ in range(number_of_lines):
    current_litres = int(input())
    if current_litres > capacity:
        print("Insufficient capacity!")
        continue
    else:
        poured_litres += current_litres
        capacity -= current_litres
print(poured_litres)
