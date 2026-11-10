import numpy as np

masiv_f32 = np.array([0.1, 0.2, 0.3], dtype=np.float32)
print("Сумма float32:", np.sum(masiv_f32))
print("Эпсилон для float32:", np.finfo(np.float32).eps)
print("Эпсилон для float64:", np.finfo(np.float64).eps)

x, y = 1.0000001, 1.0000000
print("Потеря точности:", np.float32(x) - np.float32(y))