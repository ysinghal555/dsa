class Solution:
    def printNto1(self, n):
        if n == 0:
            return
        print(n)
        self.printNto1(n - 1)


s = Solution()
s.printNto1(5)
