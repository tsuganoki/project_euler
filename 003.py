"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""

##code a function "primes" which accepts an argument, "num", and returns the first num prime numbers in order
from math import sqrt

from itertools import count

#87625999
def is_prime(n):
    for i in range(2,int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def get_big_prime_factor(num):
    primeFactorsList = []
    root = int(sqrt(num))
    if root % 2 ==0:
        root +=1
    #incriments of 2 only works because num is odd
    for i in range(3,int(sqrt(num)),2):
        print(i)
        if num % i == 0:
            if is_prime(i):
                primeFactorsList.append(i)
            elif is_prime(int(num/i)):
                primeFactorsList.append(int(num/i))
    print(primeFactorsList)
    return max(primeFactorsList)

num = 600851475147
num2 = 13195
import time
millis1 = int(round(time.time() * 1000))
print(get_big_prime_factor(num))
millis2 = int(round(time.time() * 1000))
print("seconds elapsed:", (millis2 - millis1)/1000)
