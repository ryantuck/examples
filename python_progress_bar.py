import time
from tqdm import tqdm

my_iter = range(10)

with tqdm(total=len(my_iter)) as pbar:
    for x in my_iter:
        time.sleep(1)
        pbar.update(1)
