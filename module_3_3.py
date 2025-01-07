# Задача 'Распаковка'

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['string', 1, True]
values_dict = {'a' : 1, 'b' : 'string', 'c' : False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [121, 'string_2']
print_params(*values_list_2, 42)