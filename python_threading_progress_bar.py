"""
Shows a progress bar in action while using threads.

Ripped straight from https://stackoverflow.com/questions/51601756/use-tqdm-with-concurrent-futures
"""
import time
import concurrent.futures
from tqdm import tqdm

def f(x):
    time.sleep(0.001)  # to visualize the progress
    return 2*x

def run(f, my_iter):
    l = len(my_iter)
    with tqdm(total=l) as pbar:
        # let's give it some more threads:
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = {executor.submit(f, arg): arg for arg in my_iter}
            results = {}
            for future in concurrent.futures.as_completed(futures):
                arg = futures[future]
                results[arg] = future.result()
                pbar.update(1)

my_iter = range(100000)
run(f, my_iter)
