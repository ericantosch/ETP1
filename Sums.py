import os 
import sys
import matplotlib.pyplot as plt
import numpy as np

def symSum(n):
    A = np.array([[-1, 1, 1, 1],
                    [10, 20, 0, 0],
                    [10, 0 ,30, 0],
                    [10, 0, 0, 40]])
    B = np.array([0, 20, 20, 20])
    C = np.linalg.solve(A, B)
    print(C)

if __name__ == "__main__":
    symSum(10)
