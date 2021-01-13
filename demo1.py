from multiprocessing import Pool
import numpy
from time import time
def mySquare():
    for k in range(50000):
        a = numpy.random.rand(40,40)
        b = numpy.random.rand(40,40)
        c = numpy.matmul(a,b)

def mySquare2():
    for k in range(10000):
        a = numpy.random.rand(40,40)
        b = numpy.random.rand(40,40)
        c = numpy.matmul(a,b)

if __name__ == '__main__':
    start_time = time()
    mySquare()
    elapsed_time = time() - start_time
    print("elapsed time: ", elapsed_time)

    # Runs 5 functions with 10000 operations each one

    input("Press ENTER to multiprocessing")

    p = Pool(5)             # number of workers
    start_time = time()
    p.map(mySquare2,())     # create copies of the function and assigns them to each worker
    elapsed_time = time() - start_time
    p.close()
    p.join()
    print("elapsed time: ", elapsed_time)