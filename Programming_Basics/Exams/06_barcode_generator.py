start_range = input()
end_range = input()

for a in range(int(start_range[0]), int(end_range[0]) + 1):
    for b in range(int(start_range[1]), int(end_range[1]) + 1):
        for c in range(int(start_range[2]), int(end_range[2]) + 1):
            for d in range(int(start_range[3]), int(end_range[3]) + 1):
                if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
                    print(f'{a}{b}{c}{d}', end=' ')
