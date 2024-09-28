### Multithreading
## When to use multithreading
## I/0 biund tasks: Tasks that spend more time waiting for I/O operations.
## e.g., file operations, network requests.
## Concurrent Execution : When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time


def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

## Create 2 threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)

t=time.time()
## Start the thread
t1.start()
t2.start()

## Wait for the threads to complete
t1.join()
t2.join()
finished_time=time.time()-t
print(finished_time)