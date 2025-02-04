class Solution:
    def arraySumRecur(self, n, arr):
        if n == 0:
            return 0
        return arr[n - 1] + self.arraySumRecur(n - 1, arr)

    def arraySum(self, arr):
        return self.arraySumRecur(len(arr), arr)


s = Solution()
print(s.arraySum([1, 2, 3, 4, 5]))
