n = int(input())

for index_1 in range(n):
    for index_2 in range(n):
        for index_3 in range(n):
            print(f'{chr(97 + index_1)}{chr(97 + index_2)}{chr(97 + index_3)}')