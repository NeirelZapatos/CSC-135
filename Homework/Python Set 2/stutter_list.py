# ask why this doesnt work
# def stutter_list(num_list):
#     if len(num_list) == 1:
#         num_list.append(num_list[0])
#         return num_list
#     else:
#         temp = stutter_list(num_list[:-1])
#         return temp.append(num_list[-1])

def stutter_list(num_list):
    if not num_list:
        return
    else:
        temp = num_list.pop(0)
        stutter_list(num_list)
        num_list.insert(0, temp)
        num_list.insert(0, temp)
        return num_list


print(stutter_list([1, 2, 3]))
