#!/usr/bin/python3

append_module = __import__('append')
append_to_list = append_module.append_to_list

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = append_to_list([my_list, [2, 89]])


print(new_list)
print(my_list)
