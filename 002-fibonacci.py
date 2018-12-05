"""Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding
the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose
values do not exceed four million, find the sum of the even-valued terms.



"""
from itertools import count


def fibs():
    yield 1
    yield 2
    current = 2
    prev = 1
    while True:
        yield current + prev
        (prev,current) = (current,prev+current)

sum = 0
for n in fibs():
    if n < 4e6:
        if n % 2 == 0:
            sum += n
    else:
        break
print(sum)

def populate_fibonacci():
    fibonacci = [1,2]
    for i in count():
        a = fibonacci[i]
        b = fibonacci[i+1]
        if a+b > 4e6:
            break
        fibonacci.append(a+b)
    return fibonacci


fibonacci = populate_fibonacci()

def get_sum(list):
    sum = 0
    for i in list:
        if i % 2 == 0:
            sum += i
    return sum
