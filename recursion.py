def recurse(n):
    # check for base case
    if (n <= 0):
        return 0
    else:
        # recursive case
        # print(n)
        return 1 + recurse(n-1)
recurse(10)

# Computes the sum of numbers from 0 to n
def sum(n):
    if (n <= 0):
        return 0
    else:
        # print(n)
        return n + sum(n-1)
# print(sum(5))

# Example functions to demonstrate the recursive sum for n = 3
def sumBase():
  return 0

def sum1():
  return 1 + sumBase()

def sum2():
  return 2 + sum1()

def sum3():
  return 3 + sum2()

# print the sum of 3 + 2 + 1
# print(sum3())

def is_palindrome(s):
    if (len(s) < 2):
        return True
    else:
        first = s[0]
        last = s[-1]
        if (first != last):
            return False
        else:
            middle = s[1:-1]
            return is_palindrome(middle)

# print(is_palindrome('amanaplanacanalpanama'))

def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)

# print(factorial(7))

def string_reverse(s):
    if (len(s) < 1):
        return s
    else:
        return string_reverse(s[1:]) + s[0]

# print(string_reverse('semordnilap'))

def divisor(a, b):
    if (a < 1 and b < 1):
        return 0
    else:
        if a > b:
            quotient = a / b
            remainder = a % b
            #  b / remainder
            return divisor(a - b, b)
        elif b > a:
            return divisor(a, b - a)
        # else:

# print(12 % 8)
# print(divisor(12, 8))

# Tower of Hanoi Problem
source = [[3, 2, 1], "source"]
helper = [[], "helper"]
target = [[], "target"]

def hanoi(n, source, helper, target):
    print("hanoi called with values:", n, source, helper, target)
    if n > 0:
        # move everything but the bottom disc
        hanoi(n-1, source, target, helper)
        if source:
            disk = source[0].pop()
            print("moving " + str(disk) + " from " + source[1] + " to " + target[1])
            target[0].append(disk)
        # now move the remaining stack to the target
        hanoi(n-1, helper, source, target)

hanoi(len(source[0]), source, helper, target)
