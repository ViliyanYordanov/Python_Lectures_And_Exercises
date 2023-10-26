floors = int(input())
rooms = int(input())


for floor in reversed(range(1, floors + 1)):

    for room in range(0, rooms):
        room_type = 'A' if floor % 2 else 'O'
        if floor == floors:
            room_type = 'L'
        room_number = f'{room_type}{floor}{room}'
        print(room_number, end=' ')
    print()