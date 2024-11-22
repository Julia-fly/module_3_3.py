def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
b =25
print_params(a = 1, b = b, c = True)
c = [1,2,3]
print_params(a = 1, b = b, c = c)
values_list = [1,2,3]
values_dict = {'a': 10, 'b': 20, 'c':30}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [15,25]
print_params(*values_list_2,42)
