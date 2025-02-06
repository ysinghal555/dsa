class Solution:
    def sum(self, arr, n):
        sumNum = 0

        for i in range(n):
            sumNum += arr[i]

        return sumNum
