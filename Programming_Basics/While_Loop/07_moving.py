width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())
volume = width_free_space * length_free_space * height_free_space

while True:
    data = input()

    if data == "Done":
        print(f"{volume} Cubic meters left.")
        break
    else:
        boxes = int(data)
        volume -= boxes

        if volume < 0:
            print(f"No more free space! You need {abs(volume)} Cubic meters more.")
            break