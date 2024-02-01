# import time
# import multiprocessing


# start = time.perf_counter()

# def do_smthresh():
#     print("do_smthresh....")
#     time.sleep(1)
#     print("do_smthresh finished")


# if __name__ == '__main__':
#     do_smthresh()
#     p1=multiprocessing.Process(target=do_smthresh)
#     p2=multiprocessing.Process(target=do_smthresh)
#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()
    
# finish = time.perf_counter()
# print(f"finished in {round(finish-start)}")


# import time
# import multiprocessing


# start = time.perf_counter()

# def do_smthresh():
#     print("do_smthresh....")
#     time.sleep(1)
#     print("do_smthresh finished")


# if __name__ == '__main__':
#     process = []
#     for _ in range(10):
#         p=multiprocessing.Process(target=do_smthresh, args=[_])
#         p.start()
#         process.append(p)

#     for p in process:
#         p.join()
    
#     finish = time.perf_counter()
#     print(f"finished in {round(finish-start)}")



import time
import multiprocessing
import threading


start = time.perf_counter()

def do_smthresh():
    print("do_smthresh....")
    time.sleep(1)
    print("do_smthresh finished")


if __name__ == '__main__':
    with Concurrent.futures.ThreadPoolExecutor() as executer:
        secs = [5,4,3,2,1]

    
    finish = time.perf_counter()
    print(f"finished in {round(finish-start)}")