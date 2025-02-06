import math


class Solution:
    def isPrime(self, n):
        cnt = 0

        for i in range(1, int(math.sqrt(n) + 1)):
            if n % i == 0:
                cnt += 1
                if n // i != i:
                    cnt += 1

        if cnt == 2:
            return True

        return False

    def primeUptoN(self, n):
        res = 0

        for i in range(1, n + 1):
            if self.isPrime(i):
                res += 1

        return res
