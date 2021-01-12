from multiprocessing import Pool
import numpy
from time import time

def mySquare():
    for k in range(50000):
        a = numpy.random.rand(40,40)
        b = numpy.random.rand(40,40)
        c = numpy.matmul(a,b)

start_time = time()
mySquare()
elapsed_time = time() - start_time
print("elapsed time: ", elapsed_time)