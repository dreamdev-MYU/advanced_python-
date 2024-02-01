list1 = [1,1,2,2,3,3,4,4,5,5,6]
def dublicate(my_list):
    birlik = set()
    kuplik = set()
    for i in my_list:
        if i not in birlik and i not in kuplik:
            birlik.add(i)
        else:
            birlik.discard(i)
            kuplik.add(i) 
    return list(birlik)
print(dublicate(list1))
        

