from functools import reduce

a, b, c = 100, 10, 5
result_a = reduce(lambda value, _:value +a//c ,range(2),b)
print(result_a)



# result_a = reduce(lambda acc, _: acc + b // c, range(2), a)
# print(result_a)
# result_b = reduce(lambda acc, _: acc + c, range(8), b)
# print(result_b)
# result_c = reduce(lambda acc, _: acc + 2*a - 9*c -a//a, range(2), c)
# print(result_c)

# a,b,c = 100,10,5
# for i in range(2):
#     a+=b//c
# for i in range(8):
#     b+=c
# for i in range(3):
#     c+=a-b//b
# c-=b//b
# print(a,b,c)


