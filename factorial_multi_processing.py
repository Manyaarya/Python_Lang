'''
Real World Example : Multiprocessing for CPU - Bound Tasks
Scenario: Factorial Calculation
Factorial Calculations, especially for large numbers, 
involve signifiacant computational work. Multiprocessing
can be used to distribute the workload across multiple CPU cores, improving performances.

'''

import multiprocessing
import math
import sys
import time

#Increase the maximum number of digitts for integer conversion
sys.set_int_max_str_digits(100000)

# Function to compute factorials of a given numbers

def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers=[2000,3000,4000,5000]

    start_time = time.time()

    ##Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results=pool.map(compute_factorial,numbers)

    end_time=time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")


