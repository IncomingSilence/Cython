cimport cython
cimport numpy as np
import numpy as np

np.import_array()

@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
def mandelbrot(complex c, int max_iter):
    cdef complex z = 0
    cdef int n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(double xmin, double xmax, double ymin, double ymax, int width, int height, int max_iter):
    cdef np.ndarray[np.float64_t, ndim=1] r1 = np.linspace(xmin, xmax, width)
    cdef np.ndarray[np.float64_t, ndim=1] r2 = np.linspace(ymin, ymax, height)
    cdef np.ndarray[np.int32_t, ndim=2] result = np.zeros((height, width), dtype=np.int32)
    cdef int i, j
    for i in range(height):
        for j in range(width):
            result[i, j] = mandelbrot(complex(r1[j], r2[i]), max_iter)
    return result