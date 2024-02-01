def merge_sort(mylist):
    if len(mylist)>1:
        mid = len(mylist)//2
        left_list = mylist[:mid]
        right_list = mylist[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        i=j=k=0

        while i<len(left_list) and j<len(right_list):
            if left_list[0]<right_list[j]:
                mylist[k] = left_list[i]
                i+=1
            else:
                mylist[k] = right_list[j]
                j+=1
            k+=1

        while i<len(left_list):
            mylist[k] = left_list[i]
            i+=1
            k+=1
        while i< len(right_list):
            mylist[k] = right_list[j]
            j+=1
            k+=1
    return mylist

my_list = [4,54,75,4,6,2,35,5,23,5,566,-35,5,6,56,5,3,56,5,-5,-634]
print(merge_sort(my_list))
