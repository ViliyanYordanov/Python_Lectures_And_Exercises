start_letter = input()
end_letter = input()
miss_letter = input()
counter = 0

for i in range(ord(start_letter), ord(end_letter) + 1):
    if i == ord(miss_letter):
        continue
    for j in range(ord(start_letter), ord(end_letter) + 1):
        if j == ord(miss_letter):
            continue
        for k in range(ord(start_letter), ord(end_letter) + 1):
            if k == ord(miss_letter):
                continue
            print(chr(i) + chr(j) + chr(k), end=' ')
            counter += 1
print(counter)