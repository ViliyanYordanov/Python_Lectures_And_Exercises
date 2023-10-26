amount = float(input())
coins = amount * 100

two_lv = 0
one_lv = 0
fifty_st = 0
twenty_st = 0
ten_st = 0
five_st = 0
two_st = 0
one_st = 0

while True:
    if coins >= 200:
        coins -= 200
        two_lv += 1
    else:
        break
while True:
    if coins >= 100:
        coins -= 100
        one_lv += 1
    else:
        break
while True:
    if coins >= 50:
        coins -= 50
        fifty_st += 1
    else:
        break
while True:
    if coins >= 20:
        coins -= 20
        twenty_st += 1
    else:
        break
while True:
    if coins >= 10:
        coins -= 10
        ten_st += 1
    else:
        break
while True:
    if coins >= 5:
        coins -= 5
        five_st += 1
    else:
        break
while True:
    if coins >= 2:
        coins -= 2
        two_st += 1
    else:
        break
while True:
    if coins >= 1:
        coins -= 1
        one_st += 1
    else:
        break

coins_count = two_lv + one_lv + fifty_st + twenty_st + ten_st + five_st + two_st + one_st
print(coins_count)