"""
This script highlights what a single log stream looks like
from multiple threads.
"""
import random
import time

import concurrent.futures


def sleep_random(name):
    """
    Print start/end details for log purposes.
    """
    x = random.randint(1, 4)
    print(f"thread starting: {name} {x}")
    time.sleep(x)
    print(f"thread ending: {name} {x}")


n_threads = 3
n_items = 10

items_to_process = ['thread_{n}' for n in range(n_items)]

print(f'Processing {n_items} items on {n_threads} threads')
with concurrent.futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
    executor.map(sleep_random, range(10))
