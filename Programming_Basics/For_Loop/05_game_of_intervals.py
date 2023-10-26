number_of_plays = int(input())
result = 0
a_09, a_1019, a_2029, a_3039, a_4050, a_invalid = 0, 0, 0, 0, 0, 0

for _ in range(number_of_plays):
    points = int(input())

    if 0 <= points <= 9:
        result += points * 0.2
        a_09 += 1
    elif 10 <= points <= 19:
        result += points * 0.3
        a_1019 += 1
    elif 20 <= points <= 29:
        result += points * 0.4
        a_2029 += 1
    elif 30 <= points <= 39:
        result += 50
        a_3039 += 1
    elif 40 <= points <= 50:
        result += 100
        a_4050 += 1
    if points < 0 or points > 50:
        result /= 2
        a_invalid += 1

print(f"{result:.2f}")
print(f"From 0 to 9: {a_09 / number_of_plays * 100:.2f}%")
print(f"From 10 to 19: {a_1019 / number_of_plays * 100:.2f}%")
print(f"From 20 to 29: {a_2029 / number_of_plays * 100:.2f}%")
print(f"From 30 to 39: {a_3039 / number_of_plays * 100:.2f}%")
print(f"From 40 to 50: {a_4050 / number_of_plays * 100:.2f}%")
print(f"Invalid numbers: {a_invalid / number_of_plays * 100:.2f}%")