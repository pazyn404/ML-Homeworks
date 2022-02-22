"""A*B"""

import random
import pandas as pd
import numpy as np
import timeit

def multiply(A, B):
    if len(A[0])!=len(B):
        return
    res=[[0 for j in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                res[i][j]+=A[i][k]*B[k][j]
    return res



A=[[random.random() for j in range(500)] for i in range(300)]
B=[[random.random() for j in range(200)] for i in range(500)]


res=timeit.timeit('multiply(A,B)', globals=globals(), number=1)
print(f'my multiply exucution time is {res}')

res=timeit.timeit('pd.DataFrame(data=A).dot(pd.DataFrame(data=B))', globals=globals(), number=1)
print(f'pandas multiply exucution time is {res}')

res=timeit.timeit('np.array(A).dot(np.array(B))', globals=globals(), number=1)
print(f'numpy multiply exucution time is {res}')

print('end')
