# Prime Factors

Requirements

`(a snippet)`
```
Write a class named “PrimeFactors” that has one static method: generate.
–The generate method takes an integer argument and returns a List<Integer>.
 
That list contains the prime factors in numerical sequence.
 
e.g. 
3 returns 3
8 returns 2,2,2 
10 returns 2,5
and so on.

- Jim Gildea, et. al.
```

Solution
Essentially, we will be reducing the number by dividing it to numbers from 2 to number/2. Any number higher than number/2 - except the number itself - will not yield any acceptable factors that will yield 0 remainders.
e.g. 100 -> factors will be in the range[2,50]. Anything above it until number - 1(51,52,53.....99) will not be a factor of 100.
Number is given -> get all factors -> check if it is prime -> add it to a prime_factor list -> get the quotient -> repeat until the quotient becomes a prime number -> add it to the prime_factor list.