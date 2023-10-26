n = int(input())

for index in range(1111, 10000):
    index_str = str(index)
    if int(index_str[0]) != 0 and int(index_str[1]) != 0 and int(index_str[2]) != 0 and int(index_str[3]) != 0:
        if n % int(index_str[0]) == 0 and n % int(index_str[1]) == 0 and n % int(index_str[2]) == 0 and n % int(
                index_str[3]) == 0:
            print(index_str, end=" ")
    else:
        continue
