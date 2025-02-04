class Solution:
    def NnumbersSumRecur(self, n, sumNum):
        if n == 0:
            return sumNum
        return self.NnumbersSumRecur(n - 1, sumNum + n)

    def NnumbersSum(self, n):
        return self.NnumbersSumRecur(n, 0)


s = Solution()
print(s.NnumbersSum(5))
