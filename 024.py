"""
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
 listed numerically or alphabetically, we call it lexicographic order. The
 lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

the first 362,880 start with 0
the second 362,880 start with 1

AFTER 1088640 they start with 2, so the number must start with 1 :)
 wrong_answers = [
    1672530489,
    1672804359
    ]
"""

small_list = [0,1,2,3]
medium_list = [0,1,2,3,4]
big_list = [0,2,3,4,5,6,7,8,9] #note, it is missing one, since we assume that 1 is the leading number

test_list =[ 123, 132, 213, 231, 312, 321,
            1023,1032,1203,1230,1302,1320,
            2013,2031,2103,2130,2301,2310,
            3012,3021,3102,3120,3201,3210]


"""
p1 = fact(1)
p2 = 2
p3 = 6
p4 = 24
p5 = 120
p6 = 720
p7 = 5040
p8 = 40320
p9 = 362880"""

def fact(n):
    num = 1
    while n > 0:
        num *=n
        n -=1
    return num

increment_list = [362880,40320,5040,720,120,24,6,2,1]

def get_comb(num):
    path = []
    n = 0
    i = 0
    while n < num:
        if n + increment_list[i] < num:
            n += increment_list[i]
            path.append(increment_list[i])
        elif n + increment_list[i] > num:
            i += 1
        else:
            return path
print(get_comb(1e6))

options = [5,9]
path = [2,6,6,2,
        5, 1,2,1,0]
1672804359

[362880, 362880,
40320, 40320, 40320, 40320, 40320, 40320,
5040, 5040, 5040, 5040, 5040, 5040,
720, 720,
120, 120, 120, 120, 120,
24,
6, 6,
2
]

def get_permutations(n):
    yield n
    length = len(n) -1
    i = length
    print(i)
    while True:
        n[i-1],n[i] = n[i],n[i-1]
        yield n

        if i == 2:
            i = length
        else:
            i -= 1

def test1():
    n=0
    while n < 6:
        for i in get_permutations([small_list]):
            print(i)
            n +=1
