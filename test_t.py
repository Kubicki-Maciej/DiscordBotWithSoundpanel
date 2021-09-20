import time
import threading
import concurrent.futures


start = time.perf_counter()

def x(w):
    print("sleeping 1s ")
    time.sleep(w)
    return ('done already ' + str(w))

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(x,1) for _ in range(15)]




# finish = time.perf_counter()
# print(f'Finissh in {round(finish-start, 2)} seconds')