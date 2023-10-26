tax_per_year = int(input())

basketball_shoes = tax_per_year * 60 / 100
basketball_outfit = basketball_shoes * 80 / 100
basketball_ball = basketball_outfit * 25 / 100
basketball_accessories = basketball_ball * 20 / 100

expenses = basketball_accessories + basketball_outfit + basketball_ball + basketball_shoes

print(expenses + tax_per_year)
