fortune = float(input())
year_to_be_alive = int(input())

for current_year in range(1800, year_to_be_alive + 1):
    if current_year % 2 == 0:
        fortune -= 12000
    else:
        fortune = fortune - 12000 - 50 * (current_year + 18 - 1800)

if fortune >= 0:
    print(f"Yes! He will live a carefree life and will have {fortune:.2f} dollars left." )
else:
    print(f"He will need {abs(fortune):.2f} dollars to survive.")