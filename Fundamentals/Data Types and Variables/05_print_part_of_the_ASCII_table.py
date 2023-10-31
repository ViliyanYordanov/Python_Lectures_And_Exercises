first_char = int(input())
last_char = int(input())

for index in range(first_char, last_char + 1):
    print(chr(index), end=' ')