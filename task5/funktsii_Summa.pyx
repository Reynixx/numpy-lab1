# cython: language_level=3
import numpy as np
cimport numpy as cnp

def vychislit_summu_kvadratov(cnp.ndarray[cnp.float64_t, ndim=1] arr):
    cdef int i
    cdef int n = arr.shape[0]
    cdef double summa = 0.0
    for i in range(n):
        summa += arr[i] * arr[i]
    return summa