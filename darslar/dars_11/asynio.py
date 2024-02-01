import asyncio
import time
start = time.perf_counter()
async def func1(secs):
    await asyncio.sleep(secs)
    print(f"running....{secs}")

async def main():
    async with asyncio.TaskGroup()  as tg:
        for i in range(6):
            tg.create_task(func1(i))

asyncio.run(main())

finish = time.perf_counter()
print(f"running in {round(finish-start,2)}")


# import asyncio

# async def function_one():
#     print("I'm  running...1")
# async def function_two():
#     await asyncio.sleep(5)
#     print("I'm  running...2")
# async def function_3():
#     print("I'm  running...3")
# async def function_4():
#     await asyncio.sleep(3)
#     print("I'm  running...4")

# async def main():
#     task1 = asyncio.create_task(function_one)
#     task2 = asyncio.create_task(function_two)
#     task3 = asyncio.create_task(function_3)
#     task4 = asyncio.create_task(function_4)

#     await task1
#     await task2
#     await task3
#     await task4
    
# asyncio.run(main())




# from tkinter import ttk
# import tkinter as tk
# import multiprocessing  as mp
# import time


# import time

# root = tk.Tk()
# root.geometry('500x500')

# def sleep():
#     time.sleep(10)
#     lab['text']="After run"

# btn=ttk.Button(root, text='Run', command=sleep)
# btn.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# root.mainloop()