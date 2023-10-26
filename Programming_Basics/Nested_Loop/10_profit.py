one_lv = int(input())
two_lv = int(input())
five_lv = int(input())
total = int(input())
ones = 1
twos = 2
fives = 5

for o in range(0, one_lv + 1):
    for t in range(0, two_lv + 1):
        for f in range(0, five_lv + 1):
            if o * ones + t * twos + f * fives == total:
                print(f"{o} * 1 lv. + {t} * 2 lv. + {f} * 5 lv. = {total} lv.")
