import math
import sys

def main():
    N = 1000
    x = 1.37 
    posE = sum([pow(x, k)/math.factorial(k) for k in range(0,N+1)])
    negE = sum([pow(-x, k)/math.factorial(k) for k in range(0, N+1)])
    print(posE)
    print(negE)
    testoE = sum([(pow(x, k)/math.factorial(k)) for k in range(0, N+1, 2)])
    print(testoE+pow(1.37, 2))
    print(0.5*(posE + negE))
    print(0.5*(math.exp(x) + math.exp(-x)))
    print(math.cosh(x))

if __name__ == "__main__":
    main()
    pass