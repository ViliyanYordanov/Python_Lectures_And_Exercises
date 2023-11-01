key = int(input())
lines = int(input())
word = ''
for _ in range(lines):
    letter = input()
    word += chr(ord(letter) + key)

print(word)