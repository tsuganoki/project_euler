"""The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?"""

from math import sqrt
from functools import reduce

def get_number_of_factors(num):
    factors_ct = 0
    #factors_ls = []
    for i in range(1,int(sqrt(num))):

        if num % i == 0:
            #factors_ls.append(i)
            factors_ct +=1

    factors_ct *=2
    if sqrt(num) == int(sqrt(num)):
        factors_ct +=1
    #factors_ls.append(num)
    return factors_ct



def has_n_factors(num,factors):
    if get_number_of_factors(num) > factors:
        return True
    else:
        return False



def run_it():
    triangle = 0
    num = 1
    latest_max = 0
    while get_number_of_factors(triangle) < 500:

        triangle +=num
        print("triangle: ",triangle,"factors: ",get_number_of_factors(triangle))
        if get_number_of_factors(triangle) > latest_max:
            latest_max = get_number_of_factors(triangle)

        num += 1

    print("done! Final triangle: ", triangle)

#print("new test: ", has_n_factors(28,5))
run_it()


#print(get_number_of_factors(25))
