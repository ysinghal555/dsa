class Solution:
    def countOdd(self, arr, n):
        cnt = 0
        for i in range(n):
            if arr[i] % 2 != 0:
                cnt += 1

        return cnt
