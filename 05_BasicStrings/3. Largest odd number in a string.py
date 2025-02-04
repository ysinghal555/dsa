class Solution:
    def largeOddNum(self, s):
        n = len(s)
        for i in range(n-1, -1, -1):
            if int(s[i]) % 2 != 0:
                return str(int(s[:i+1:]))

        return "" 