from multiprocessing import Pool, Array
import random
import time
import math

# method to do multiplication of matrix
from multiprocessing.context import Process


def matrixMul(A, itr, block, size, col, result):
    # start a loop to loop size of the block
    for i in range (0, block):
        # temp var
        temp = 0
        # loop range of from 0 to size of column
        for j in range (0, size):
            # A[itr * block + i]
            # e.g. itr = 0, block = 4
            # 0*4 = 0 -> 0 + i -> where i = 0 - (n-1)
            # e.g. itr = 1, block = 4
            # 1 * 4 = 4 -> 4 + i -> where i = 0 - (n-1)
            temp = temp + A[itr * block + i][j] * col[j]
        result[itr * block + i] = temp
        time.sleep((1/size));


if __name__ == '__main__':
    # get input
    n = int(input("Enter number of nodes: "))
    # empty list of arrays
    matrix = []
    # loop and append an array of ints (i) of random numbers from j to n where it ents n numbers into that array
    for i in range (0, n):
        # append a new array of random n ints into list
        matrix.append(Array('i', [int(random.random() * 10) for j in range(0, n)]))
    # Debug Array
    """
    print('start matrix')
    for i in range(0,n):
        for j in range (0, n):
            # end="" makes it so it does not print a newline
            print(matrix[i][j], end=" ")
        print('\n')
        print('end matrix')
    """
    # created array of columns with random numbers
    columns = Array('i', [int(random.random() * 10) for j in range(0, n)])
    # debug
    """
    print('start col')
    for j in range(0, n):
        # end="" makes it so it does not print a newline
        print(columns[j])
    print('end col')
    """
    # created array to hold results
    result = Array('i', n)
    # get break down of how many rows per process
    size = int(n / 4)
    # create each process
    p0 = Process(target=matrixMul, args=(matrix, 0, size, n, columns, result))
    p1 = Process(target=matrixMul, args=(matrix, 1, size, n, columns, result))
    p2 = Process(target=matrixMul, args=(matrix, 2, size, n, columns, result))
    p3 = Process(target=matrixMul, args=(matrix, 3, size, n, columns, result))
    # start processes
    p0.start()
    p1.start()
    p2.start()
    p3.start()
    # wait for processes to finish
    p0.join()
    p1.join()
    p2.join()
    p3.join()
    """
    # debug
    print("test")
    for i in range (0,n):
        print(result[i])
    """
















