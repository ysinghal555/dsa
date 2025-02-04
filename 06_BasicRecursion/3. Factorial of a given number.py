class Solution:
    def factorialRecur(self, n, fact):
        if n == 1:
            return fact
        return self.factorialRecur(n - 1, fact * n)

    def factorial(self, n):
        return self.factorialRecur(n, 1)


s = Solution()
print(s.factorial(6))
