class Solution:
    def lastChar(self, s):
        n = len(s)
        if n <= 0:
            return -1

        return s[n - 1:]