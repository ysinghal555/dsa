class Solution:
    def isPalindrome(self, n):
        rev = 0
        num = n

        while n != 0:
            rem = n % 10
            rev = rev * 10 + rem
            n = n // 10

        if rev == num:
            return True

        return False
