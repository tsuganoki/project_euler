"""Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_multiples(a,b,n):
    lis = []
    for i in range(n):
        if i % a == 0 or i % b ==0:
            lis.append(i)
    #print(lis)
    return sum(lis)


print(sum_multiples(3,5,1000))
