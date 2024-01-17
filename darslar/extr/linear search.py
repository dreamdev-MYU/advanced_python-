
# my_list = [7,5,43,65,45,543,6,6,346,5,6467,4,46]
# def quick_sort(list_a) :
#     length = len(list_a)
#     if length<2:
#         return list_a
#     else:
#         pivot = list_a.pop()
#         left_list = []
#         right_list = []
#         for i in list_a:
#             if pivot<i:
#                 right_list.append(i)
#             else:
#                 left_list.append(i)
#         return quick_sort(left_list)+[pivot]+quick_sort(right_list)
# print(quick_sort(my_list))
    





# massiv = [0.3, 0.7, 23, 21, 0.6, 23, -0.3, 4, 0.5, 54, 5, 34, 4]
# def funk(massiv):
#     a = len(massiv)
#     new = []
#     for i in range(a):
#         if 0 < massiv[i] < 1:
#             new.append(f"{massiv[i]} soni {i}-chi indexda joylashgan")
#     if new:
#         return new
#     else:
#         return "Mavjud emas"
# print(funk(massiv))


















# import hashlib
# def shifrlash(ism, familya):
#     ism_familya = ism + familya
#     shifrlangan = hashlib.sha256(ism_familya.encode()).hexdigest()
#     return shifrlangan
# ism = input("Ismingizni kiriting: ")
# familya = input("Familyangizni kiriting: ")
# shifrlangan_qiymat = shifrlash(ism, familya)
# print(f"Ismingiz va familyangiz shifrlangan natija: {shifrlangan_qiymat}")




# def qidiruv():
#     target = "D"
#     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
#     for i in range(len(alphabet)):
#         count = 0
#         if alphabet[i] == target:
#             count += 1
#             return f"Harf {target} mavjud va {i+1} chi urinishda topildi"
    
#     return "Qidirilayotgan harf jadvalda mavjud emas"

# print(qidiruv())
