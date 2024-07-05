"""
module_3_3.py

Задача "Распаковка"
"""

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(2, 'second', False)  #1
print_params("это возможная опечатка", False)
print_params('one param')
print_params()
print_params([1, 2, 3])
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [True, 2, 'list2']  #2
values_dict = {'a': True, 'b': 3, 'c': 'list__3'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [4.54, (2, 3)]  #3
print_params(*values_list_2, 42)

#-module_3_3.py
