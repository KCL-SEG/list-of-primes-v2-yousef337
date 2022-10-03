from math import sqrt, floor, log, ceil
"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

convergenceThershold = 0.5

def isPrime(n: int) -> bool:
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def approximateInversePIFunction(y: int) -> int:
    xOld = 0
    x = y*log(y)
    while(x - xOld > convergenceThershold):
        xOld = x
        x = y * log(x)
    return ceil(x)

def primes(number_of_primes):
    if (number_of_primes < 1):
        raise ValueError()

    list = []
    approximableRegionCeil = approximateInversePIFunction(number_of_primes)
    primeLocationList = [True if i > 1 else False for i in range(approximableRegionCeil + 1)]
    currentIteration: int = 2

    while currentIteration <= approximableRegionCeil and len(list) < number_of_primes:
        if (primeLocationList[currentIteration]):
            list.append(currentIteration)
            for j in range(currentIteration * currentIteration, approximableRegionCeil + 1, currentIteration):
                primeLocationList[j] = False
        
        currentIteration += 1

    while len(list) < number_of_primes:
        if isPrime(currentIteration):
            list.append(currentIteration)
        currentIteration += 1

    return list
