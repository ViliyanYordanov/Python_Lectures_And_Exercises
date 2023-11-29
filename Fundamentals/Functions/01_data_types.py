def data_type(a_string, a_value):
    if a_string == 'int':
        return int(a_value) * 2
    elif a_string == 'real':
        return f'{float(a_value) * 1.5:.2f}'
    elif a_string == 'string':
        return f'${a_value}$'


the_string = input()
the_value = input()
print(data_type(the_string, the_value))