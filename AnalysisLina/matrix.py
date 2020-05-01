import math
import sys
import numpy as np


def main():
    A = np.array([[1, 1, -1],
                    [35, -25, 0],
                    [0, 25, 80]])
    B = np.array([0, -9, 24])

    C = np.linalg.solve(A, B)
    print(C)
    print(5.8*(1/26))




if __name__ == "__main__":
    main()