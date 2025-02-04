## Multithreading with Thread Pool Executor
## Managing threads

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
    time.sleep(1)
    return f"Number :{number}"

numbers=[1,2,3,4,5,7,8,9,10,1,2,2]

with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_numbers, numbers)

for result in results:
    print(result)