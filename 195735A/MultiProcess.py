import numpy as np
import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import freeze_support

ns = list(np.arange(1, 11))


def task(_n):
    s = 0
    for i in range(1, _n+1):
        s += i
        time.sleep(0.1)
    return s


if __name__ == '__main__':
    freeze_support()
    start = time.time()

    with ProcessPoolExecutor(6) as e:
        ret = e.map(task, ns)
    multiPro = [r for r in ret]

    end = time.time()
    delta = end - start
    print('処理時間:{}s'.format(round(delta, 3)))
