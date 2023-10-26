width = int(input())
length = int(input())
total_peaces = width * length

while True:
    data = input()

    if data == 'STOP':
        print(f"{total_peaces} pieces are left." )
        break
    else:
        taken_peaces = int(data) #21
        total_peaces -= taken_peaces #-1

        if total_peaces < 0:
            print(f"No more cake left! You need {abs(total_peaces)} pieces more.")
            break
