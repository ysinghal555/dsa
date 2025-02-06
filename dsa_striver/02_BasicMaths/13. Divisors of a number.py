import math


class Solution:
    def divisors(self, n):
        ans = []

        for i in range(1, int(math.sqrt(n) + 1)):
            if n % i == 0:
                ans.append(i)
                if n // i != i:
                    ans.append(n // i)

        ans.sort()
        return ans
