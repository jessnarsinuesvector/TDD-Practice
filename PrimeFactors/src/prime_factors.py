class PrimeFactors:
    def __init__(self):
        pass

    def generate(self, num: int) -> list[int]:
        orig_num = num
        prime_factors = []
        while not self.__is_prime_number(num):
            start = 2
            end = int(num/2) + 1
            for i in range(start, end):
                if num % i == 0 and self.__is_prime_number(i):
                    prime_factors.append(i)
                    num = int(num / i)
                    break
        prime_factors.append(num)
        print("Prime factors of {} are {}".format(orig_num, prime_factors))
        return prime_factors

    def __get_factors(self, num: int) -> list[int]:
        factors = [num]
        for i in range(1, int(num/2) + 1):
            if num % i == 0:
                factors.append(i)
        return sorted(factors)

    def __is_prime_number(self, num: int) -> list[int]:
        factors = self.__get_factors(num)
        if len(factors) > 2 or num == 1:
            return False
        return True