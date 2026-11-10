import numpy as np
import time
from scipy.sparse import csr_matrix, random

mat_csr = csr_matrix((np.array([1.0, 2.0, 3.0, 4.0, 5.0]), (np.array([0, 1, 2, 3, 4]), np.array([1, 0, 4, 2, 3]))), shape=(5, 5))
print("CSR матрица:\n", mat_csr.toarray())
print("COO формат:\n", mat_csr.tocoo().toarray())
print("CSC формат:\n", mat_csr.tocsc().toarray())

v = np.array([1, 2, 3, 4, 5], dtype=float)
print("Результат умножения на вектор:", mat_csr.dot(v))

n = 1000
sp = random(n, n, density=0.01, format='csr')
dn = sp.toarray()
vec = np.random.rand(n)

t0 = time.time(); sp.dot(vec); print("Время для разреженной матрицы:", time.time() - t0)
t0 = time.time(); np.dot(dn, vec); print("Время для плотной матрицы:", time.time() - t0)