class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        sumOfN = (n * (n + 1)) // 2
        sumNum = 0

        for i in range(n):
            sumNum += arr[i]

        return sumOfN - sumNum
