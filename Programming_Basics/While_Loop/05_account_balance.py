total = 0

while True:
    data = input()

    if data == 'NoMoreMoney':
        break
    elif float(data) < 0:
        print("Invalid operation!")
        break
    else:
        total += float(data)
        print(f"Increase: {float(data):.2f}")
print(f"Total: {total:.2f}")
