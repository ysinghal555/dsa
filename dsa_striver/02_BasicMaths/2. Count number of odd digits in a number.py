class Solution:
    def countOddDigit(self, n):
        cnt = 0

        while n != 0:
            rem = n % 10
            if rem % 2 != 0:
                cnt += 1
            n = n // 10

        return cnt