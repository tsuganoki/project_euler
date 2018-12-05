"""Surprisingly there are only three numbers that can be written as the sum of fourth power of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""


#wrongAnswers9999 = [4150, 4151],8301
#wrongAnswers99999= [4150, 4151, 54748, 92727, 93084] 248860
# right answer = [4150, 4151, 54748, 92727, 93084, 194979], 443839


# I'm naming this property "magic"

def is_magic(n,power):
    total = 0
    for i in str(n):
        total += int(i)**power
    print(total)
    if n == total:
        return True
    return False

print(is_magic(1634,4))
print(is_magic(8208,4))
print(is_magic(9474,4))
print(is_magic(11111,5))

def testOne(limit,power):
    magicNumbers = []
    for i in range(10,limit):
        if is_magic(i,power):
            print("adding",i)
            magicNumbers.append(i)
    return magicNumbers

magicNumbers = testOne(9999999,5)
print(magicNumbers)
print("total is:", sum(magicNumbers))
