"""Method 1 (using set)"""


class Solution:
    def removeDuplicates(self, arr):
        n = len(arr)
        res = set()

        for i in range(n):
            res.add(arr[i])

        return len(res)


"""Method 2 (Inplace)"""


class Solution:
    def removeDuplicates(self, arr):
        n = len(arr)
        j = 0

        for i in range(1, n):
            if arr[i] != arr[j]:
                arr[j + 1], arr[i] = arr[i], arr[j + 1]
                j += 1

        return j + 1
