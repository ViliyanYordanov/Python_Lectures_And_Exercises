while True:
    string = input()

    if string == 'End':
        break
    if string == 'SoftUni':
        continue
    for i in range(len(string)):
        for _ in range(0, 2):
            print(string[i], end='')
    print()

    # while True:
    #     command = input()
    #     double_string = ''
    #     if command == 'End':
    #         break
    #     if command == 'SoftUni':
    #         continue
    #     for i in range(len(command)):
    #         double_string += command[i] * 2
    #     print(double_string)
