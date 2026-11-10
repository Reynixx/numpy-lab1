import numpy as np
A = np.arange(20).reshape(4, 5)

print("Вторая строка:", A[1, :])
print("Столбец с индексом 3:", A[:, 3])
print("Подмассив из строк 1-3 и столбцов 2-4:\n", A[1:4, 2:5])
print("Fancy-индексация:\n", A[[0, 2, 3]][:, [1, 4]])

A_neg = np.array([[-1, 2, -3], [4, -5, 6]])
A_neg[A_neg < 0] = 0
print("Без отрицательных элементов:\n", A_neg)

B = np.array([[1], [2], [3], [4]])
C = np.array([[10, 20, 30, 40, 50]])
print("Результат broadcasting:\n", B + C)