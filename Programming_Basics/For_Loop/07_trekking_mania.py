groups = int(input())

peak_1, peak_2, peak_3, peak_4, peak_5, = 0, 0, 0, 0, 0

for _ in range(groups):
    climbers = int(input())

    if climbers <= 5:
        peak_1 += climbers
    elif 5 < climbers <= 12:
        peak_2 += climbers
    elif 12 < climbers <= 25:
        peak_3 += climbers
    elif 25 < climbers <= 40:
        peak_4 += climbers
    elif 40 < climbers:
        peak_5 += climbers

all_climbers = peak_1 + peak_2 + peak_3 + peak_4 + peak_5

print(f'{(peak_1 / all_climbers * 100):.2f}%')
print(f'{(peak_2 / all_climbers * 100):.2f}%')
print(f'{(peak_3 / all_climbers * 100):.2f}%')
print(f'{(peak_4 / all_climbers * 100):.2f}%')
print(f'{(peak_5 / all_climbers * 100):.2f}%')