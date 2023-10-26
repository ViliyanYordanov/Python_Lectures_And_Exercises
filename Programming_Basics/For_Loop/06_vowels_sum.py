word = input()

total = 0

a = 1
e = 2
i = 3
o = 4
u = 5

for char in word:
    if char == 'a':
        total = total + a
    elif char == 'e':
        total = total + e
    elif char == 'i':
        total = total + i
    elif char == 'o':
        total = total + o
    elif char == 'u':
        total = total + u
print(total)