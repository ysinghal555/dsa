"""Brute"""


class Solution:
    def isPerfect(self, n):
        divisors = []

        for i in range(1, (n // 2) + 1):
            if n % i == 0:
                divisors.append(i)

        if sum(divisors) == n:
            return True
        return False


"""Optimal"""
import math


class Solution:
    def isPerfect(self, n):
        sumNum = 0

        if n == 1:
            return False

        for i in range(1, int(math.sqrt(n) + 1)):
            if n % i == 0:
                sumNum += i
                if n // i != i:
                    sumNum += (n // i)

        if sumNum - n == n:
            return True

        return False
