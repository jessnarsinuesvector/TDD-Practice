import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from PrimeFactors.src.prime_factors import PrimeFactors

if __name__ == "__main__":
    prime_factors = PrimeFactors()
    input_nums = [
        3,
        8,
        10
    ]
    for i in input_nums:
        prime_factors.generate(i)