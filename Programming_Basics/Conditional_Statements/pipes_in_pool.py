v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_litres = p1 * h
p2_litres = p2 * h
water_level = p1_litres + p2_litres

if water_level <= v:
    print(f"The pool is {water_level / v * 100:.2f}% full. "
                f"Pipe 1: {p1_litres / water_level * 100:.2f}%. Pipe 2: {p2_litres / water_level * 100:.2f}%.")
else:
    print(f"For {h} hours the pool overflows with {water_level - v:.2f} liters.")
