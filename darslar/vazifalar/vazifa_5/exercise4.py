my_list = [3,0,1,4,5]
def quick_sort(my_list):
    a = len(my_list)
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
        numbers =  quick_sort(left_list)+[pivot]+quick_sort(right_list)
        return numbers
def func(numbers):       
    for i in range(numbers[-1]):
        if i not in numbers:
            return i
list2 = quick_sort(my_list)
print(func(list2))





