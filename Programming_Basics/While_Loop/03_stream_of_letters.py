c_flag = False
o_flag = False
n_flag = False

secret_flag = False

c_counter = 0
o_counter = 0
n_counter = 0

word = ''

while True:
    if o_flag and c_flag and n_flag:
        secret_flag = True
    if secret_flag:
        print(word + ' ', end='')
        word = ''
        c_flag = False
        o_flag = False
        n_flag = False
        secret_flag = False
        c_counter = 0
        o_counter = 0
        n_counter = 0
        continue
    letter = input()

    if letter == 'End':
        break

    if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:

        if letter == 'c' and c_counter == 0:
            c_flag = True
            c_counter += 1
            continue
        if letter == 'o' and o_counter == 0:
            o_flag = True
            o_counter += 1
            continue
        if letter == 'n' and n_counter == 0:
            n_flag = True
            n_counter += 1
            continue
        word += letter
    else:
        continue
