number_of_lines = int(input())
total = 0

for char in range(number_of_lines):
    character = input()
    total += ord(character)
print(f"The sum equals: {total}")