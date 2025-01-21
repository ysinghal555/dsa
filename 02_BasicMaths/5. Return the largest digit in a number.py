class Solution:
    def largestDigit(self, n):
        largestNum = 0

        while n != 0:
            rem = n % 10
            if rem > largestNum:
                largestNum = rem
            n = n // 10

        return largestNum
