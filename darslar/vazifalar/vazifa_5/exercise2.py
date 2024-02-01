def str_difference(my_text, my_text1):
    new = []
    min_length = min(len(my_text), len(my_text1))
    for i in range(min_length):
        if my_text[i] != my_text1[i]:
            new.append(my_text[i])
    if len(my_text) > len(my_text1):
        new.extend(my_text[min_length:])
    elif len(my_text1) > len(my_text):
        new.extend(my_text1[min_length:])

    return ''.join(new)

my_text = "abcde"
my_text1 = "abc"
result = str_difference(my_text, my_text1)
print(result)









