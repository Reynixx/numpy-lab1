import numpy as np
import timeit

mm = np.memmap("temp_array.dat", dtype="float64", mode="w+", shape=(1000, 1000))
mm[:] = np.random.rand(1000, 1000)
mm.flush()
del mm

print("Чтение строки:", np.memmap("temp_array.dat", dtype="float64", mode="r", shape=(1000, 1000))[10, :5])
print("Чтение столбца:", np.memmap("temp_array.dat", dtype="float64", mode="r", shape=(1000, 1000))[:5, 10])

kod_row = "import numpy as np; mm = np.memmap('temp_array.dat', dtype='float64', mode='r', shape=(1000, 1000)); s = sum(mm[i, j] for i in range(1000) for j in range(1000)); del mm"
kod_col = "import numpy as np; mm = np.memmap('temp_array.dat', dtype='float64', mode='r', shape=(1000, 1000)); s = sum(mm[i, j] for j in range(1000) for i in range(1000)); del mm"

print("Обход по строкам: Row:", timeit.timeit(kod_row, number=1))
print("Обход по столбцам: Column:", timeit.timeit(kod_col, number=1))