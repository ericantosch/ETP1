import math
import sys
import numpy as np


def main():
    """ A = np.array([[2, -10],
                    [10, -8.7]])

    B = np.array([39,-3]) """

    A = np.array([[1, -1, 1],
                    [8, 10, 0],
                    [0, 10, 999999]])

    B = np.array([0,39, 23])
    C = np.linalg.solve(A, B)
    print(C)
    print(5.8*(1/26))




if __name__ == "__main__":
    main()