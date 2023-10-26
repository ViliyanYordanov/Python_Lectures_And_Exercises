a = int(input())
b = int(input())

for i in range(a, b + 1):
    for j in range(a, b + 1):
        for l in range(a, b + 1):
            for m in range(a, b + 1):

                while i > m and (j + l) % 2 == 0:
                    if i % 2 == 0 and m % 2 != 0:
                        print(f'{i}{j}{l}{m} ', end="")
                        break
                    elif i % 2 != 0 and m % 2 == 0:
                        print(f'{i}{j}{l}{m} ', end="")
                        break
                    else:
                        break