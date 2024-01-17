from collections import namedtuple
mentor = namedtuple("mentor",["name", "age", "group"])
new_tuple = mentor("Yahyobek","20","FN7")
print(new_tuple)
print(new_tuple._replace(name = "asrorbek"))


# class Mentor:

