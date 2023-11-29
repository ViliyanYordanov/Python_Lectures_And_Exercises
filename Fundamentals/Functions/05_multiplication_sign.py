def multiplication_sign(num1, num2, num3):
    negative_counter = 0
    zero_flag = False

    if num1 == 0:
        zero_flag = True
    elif num1 < 0:
        negative_counter += 1

    if num2 == 0:
        zero_flag = True
    elif num2 < 0:
        negative_counter += 1

    if num3 == 0:
        zero_flag = True
    elif num3 < 0:
        negative_counter += 1

    if zero_flag:
        print('zero')
    elif negative_counter % 2 == 0:
        print('positive')
    else:
        print('negative')


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
multiplication_sign(number_1, number_2, number_3)