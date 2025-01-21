import time
import Cython_Fraktal

if __name__ == "__main__":
    start_time = time.time()
    Cython_Fraktal.mandelbrot_set(-2.0, 1.0, -1.5, 1.5, 1000, 1000, 1000)
    execution_time = time.time() - start_time
    print("Cython execution time: {:.2f} seconds".format(execution_time))