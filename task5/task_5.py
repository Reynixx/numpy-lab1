import time
import numpy as np
from funktsii_Summa import vychislit_summu_kvadratov

arr = np.random.rand(10**7)
lst = arr.tolist()

t0 = time.time()
py_res = sum(x * x for x in lst)
t_py = time.time() - t0

t0 = time.time()
cy_res = vychislit_summu_kvadratov(arr)
t_cy = time.time() - t0

print(f"Python: {t_py:.4f} сек")
print(f"Cython: {t_cy:.4f} сек")
print(f"Ускорение в {t_py / t_cy:.1f} раз(а)")