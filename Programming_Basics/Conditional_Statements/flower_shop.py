from math import floor
from math import ceil

m_number = int(input())
z_number = int(input())
r_number = int(input())
k_number = int(input())
present_price = float(input())

m_price = m_number * 3.25
z_price = z_number * 4
r_price = r_number * 3.50
k_price = k_number * 8
total = m_price + z_price + r_price + k_price
tax = total * 0.05
income = total - tax

if present_price <= income:
    print(f"She is left with {floor(income - present_price)} leva." )
else:
    print(f"She will have to borrow {ceil(present_price - income)} leva." )
