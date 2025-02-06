"""Method 1 (Using a new Array)"""


class Solution:
    def moveZeroes(self, arr):
        n = len(arr)
        tempArr = [0] * n
        j = 0
        for i in range(n):
            if arr[i] != 0:
                tempArr[j] = arr[i]
                j += 1

        return tempArr


s = Solution()
print(s.moveZeroes([0, 1, 4, 0, 5, 2]))

"""Method 2 (inplace)"""


class Solution:
    def moveZeroes(self, arr):
        n = len(arr)
        j = -1

        # Check if 0 exist or not
        for i in range(n):
            if arr[i] == 0:
                j = i
                break

        # Means that 0 does not exist in the array
        if j == -1:
            return arr

        for i in range(j + 1, n):
            if arr[i] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1

        return arr
