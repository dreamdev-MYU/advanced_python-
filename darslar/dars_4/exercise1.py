my_list = [1,4,35,5,2,-53,5,-3,5,-35,35,53,45,3]
def quick_sort(my_list):
    a=len(my_list)
    if a<2:
        return my_list
    else:
        pivot = my_list.pop()
        left_list = []
        right_list = []
        for i in my_list:
            if pivot<i:
                right_list.append(i)
            else:
                left_list.append(i)
        return quick_sort(left_list)+[pivot]+quick_sort(right_list)
print(quick_sort(my_list))
        

