list1 = [1,2,3,4,5,4,3,2,3,4,5,6,7,8]
def find_dubllicate(my_list):
    remove_d = set()
    new = []
    for i in range(len(my_list)):
        if my_list[i] in remove_d:
            new.append(i)
        else:
            remove_d.add(my_list[i])
    for index in reversed(new):
        my_list.pop(index)

    my_list.extend(['_'] * len(new))
    return my_list
result = find_dubllicate(list1)
print(result)
