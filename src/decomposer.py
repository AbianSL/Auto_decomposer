#  @file main.py
#  @author AbianSL
#  @brief decomposer the input image into prime numbers
#  @version 0.1
#  @date 2024-07-22

import math

def decomposer(number: int) -> list:
    """
    Decompose the input number into prime numbers
    """
    primes = []
   
    while number % 2 == 0:
        primes.append(2)
        number = number // 2

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            primes.append(i)
            number = number // i

    if number > 2:
        primes.append(number)

    return primes
