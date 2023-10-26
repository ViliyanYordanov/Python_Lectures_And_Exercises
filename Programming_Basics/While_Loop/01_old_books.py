desired_book = input()
books_counter = 0

while True:
    current_book = input()

    if current_book == 'No More Books':
        print("The book you search is not here!")
        print(f"You checked {books_counter} books.")
        break
    if current_book != desired_book:
        books_counter += 1
    else:
        print(f"You checked {books_counter} books and found it.")
        break

