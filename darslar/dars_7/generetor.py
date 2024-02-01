import random
import time

names = ["asadbek","Hasanboy","Asrorbek","Ilyosbek","Farruxbek"]
major = ["IT","Filologiya","tarix","iqtisod","medik","Jismoniy tarbiya","boshlangich"]
def people_list(people_num):
    result = []
    for i in range(people_num):
        person = {
            "id":1,
            "name":random.choice(names),
            "majors":random.choice(major)
        }
        result.append(person)
        return result
time1 = time.time()
people = people_list(1000000000)
time2 = time.time()
print("funksiya tzligi {} ".format({time2-time1}))
