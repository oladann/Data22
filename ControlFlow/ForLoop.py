list_data = [1, 2, 3, 4, 5]

# for num in list_data:
#     print(num*2)

# embedded_list = [[1, 2, 3], [4,5,6]]
# for data in embedded_list:
#     print(data)
#     for num in data:
#         print(num)

dict_data = {1: {"name": "Brosnson", "money": "£0.50"}, 2: {"name": "Masha", "Money": "£3.66"}, 3: {"name": "Yoad", "Money": "£1.00"}}


# for i in dict_data.keys():
#     for value in dict_data[i].values():
#         print(f"{i} {value}")


# for item in dict_data.values():
#     for subitem in item.values():
#         print(subitem)
#
#
# dictionary_variable = {"Theo": "Gluckstein", "Aaron":"Davis", "Amy": "Zhang"}
#
# for name in dictionary_variable.values():
#     print(name)

list_numbers = [1, 2, 3, 4, 5]

for num in list_numbers:
    if num == 3:
        print("I found 3!")
    elif num > 3:
        print("gone too far")
    else:
        print("too soon")