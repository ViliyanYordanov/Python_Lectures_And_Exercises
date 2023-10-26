months = int(input())
total = 0
water = 20
wifi = 15
total_electricity = 0
total_water = months * water
total_wifi = months * wifi
total_others = 0

for _ in range(months):
    electricity = float(input())
    total_electricity += electricity
    others = (electricity + water + wifi) * 1.2
    total_others += others
    total += electricity + water + wifi + others

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_wifi:.2f} lv")
print(f"Other: {total_others:.2f} lv")
# print(f"Average: {(total_electricity + total_water + total_wifi + total_others) / months:.2f} lv")
print(f"Average: {total / months:.2f} lv")
