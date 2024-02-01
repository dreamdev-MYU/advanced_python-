import time 
import threading
import concurrent.futures

def do_smth():
     print("reading a file...")
     time.sleep(1)
     print("Complated reading")

with concurrent.futures.ThreadPoolExecutor() as executer:
    list_a = [3,5,2,53,5]
    res = executer.map(do_smth,list_a)









# start = time.perf_counter


# thread = []

# for _ in range(30):
#     t =threading.Thread(target = do_smth)
#     t.start()
#     thread.append(t)

# for t in thread:
#      t.join()

# t1 = threading.Thread(target = do_smth)
# t2 = threading.Thread(target = do_smth)
# t3 = threading.Thread(target = do_smth)

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()


