"""Method 1 (Using posArr and negArr)"""
class Solution:
    def rearrangeArray(self, arr):
        n = len(arr)
        posArr = []
        negArr = []

        for i in range(n):
            if arr[i] >= 0:
                posArr.append(arr[i])
            else:
                negArr.append(arr[i])

        i = 0
        j = 0
        k = 0

        while k < n:
            arr[k] = posArr[i]
            arr[k + 1] = negArr[j]
            k += 2
            i += 1
            j += 1

        return arr


s = Solution()
print(s.rearrangeArray([2, 4, 5, -1, -3, -4]))
