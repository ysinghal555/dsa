class Solution:
    def palindromeCheckRecur(self, s, i, n):
        if i >= n // 2:
            return True

        if s[i] != s[n - i - 1]:
            return False

        return self.palindromeCheckRecur(s, i + 1, n)

    def palindromeCheck(self, s):
        return self.palindromeCheckRecur(s, 0, len(s))
