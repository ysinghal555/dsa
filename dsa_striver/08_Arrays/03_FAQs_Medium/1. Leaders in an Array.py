class Solution:
    def leaders(self, arr):
        n = len(arr)

        if n == 0:
            return arr

        res = [arr[-1]]
        maxEle = arr[-1]

        for i in range(n - 1, -1, -1):
            if arr[i] > maxEle:
                maxEle = arr[i]
                res.append(maxEle)
        res.reverse()
        return res


s = Solution()
print(s.leaders([1, 2, 5, 3, 1, 2]))
