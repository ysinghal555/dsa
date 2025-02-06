class Solution:
    def findMaxConsecutiveOnes(self, arr):
        n = len(arr)
        cnt = 0
        maxOnes = 0

        for i in range(n):
            if arr[i] == 1:
                cnt += 1
            elif arr[i] == 0:
                cnt = 0
            maxOnes = max(cnt, maxOnes)

        return maxOnes
