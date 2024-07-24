import unittest

from PrimeFactors.src.prime_factors import PrimeFactors


class TestPrimeFactor(unittest.TestCase):
    def setUp(self):
        self.primefactors = PrimeFactors()

    def test_can_return_prime_factors_successfully(self):
        self.assertListEqual(self.primefactors.generate(3), sorted([3]))
        self.assertListEqual(self.primefactors.generate(8), sorted([2, 2, 2]))
        self.assertListEqual(self.primefactors.generate(10), sorted([5, 2]))
        self.assertListEqual(self.primefactors.generate(20), sorted([2, 2, 5]))
        self.assertListEqual(self.primefactors.generate(100), sorted([2, 2, 5, 5]))
        self.assertListEqual(self.primefactors.generate(1000), sorted([2, 2, 2, 5, 5, 5]))