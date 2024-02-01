import time
import os

def query():
    for i in os.walk('C:\\'):
        print(i[0])
        time.sleep(1)

query()