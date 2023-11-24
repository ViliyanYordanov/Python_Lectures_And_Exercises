def round_function(my_list):
    rounded_numbers_list = []
    for n in primal_list:
        rounded_numbers_list.append(round(float(n)))

    return rounded_numbers_list


primal_list = input().split()
print(round_function(primal_list))
