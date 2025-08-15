import numpy as np
import math
import random

def test1():
    array = np.array([[[1,2],[3,4]],
                [[1,2],[3,4]]])
    print(array.ndim)#dimentions
    print(array.shape)#shape
    print(array.size == math.prod(array.shape))#size
    print(array.dtype)#data type int for integer,64 for 64 bit

def test2():
    print(np.zeros(2))
    print(np.ones(3))
    print(np.empty(2))
    print(np.arange(6))
    print(np.linspace(0,10,num=5))
    print(np.ones(2,dtype=np.int64))

def test3():
    array = np.array([1,2,5,3,76,6,4])
    print(np.sort(array))
    a = np.array([1,2,3,4])
    b = np.array([7,8,9])
    print(np.concatenate((a,b)))
    # c = np.array([[2,3,4],[6,7,8]])
    # print(np.concatenate((c,b),axis=0))
    print(array.shape)
    row_vector = array[np.newaxis,:]
    col_vector = array[:,np.newaxis]
    print(row_vector,'\n',col_vector)

a = np.arange(1,13)
a = a.reshape(3,4)
print(a)
print(a[(a%3==0)&(a>5)])
print((a>5) | (a%2==0))