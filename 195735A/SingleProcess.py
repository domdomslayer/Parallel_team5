import numpy as np
import time

ns = list(np.arange(1, 11))  # 数字のリストを作成


def task(_n):
    s = 0
    for i in range(1, _n+1):
        s += i
        time.sleep(0.1)
    return s


start = time.time()  # 処理開始時間

single = []
for n in ns:
    single.append(task(n))

end = time.time()  # 処理終了時間
delta = end - start  # 処理時間
print('処理時間:{}s'.format(round(delta, 3)))
