"""Method 1"""


class Solution:
    def get_min_max(self, arr):
        n = len(arr)
        minEle = float('inf')

        for i in range(n):
            minEle = min(arr[i], minEle)

        maxEle = float('-inf')

        for i in range(n):
            maxEle = max(arr[i], maxEle)

        return [minEle, maxEle]


"""Method 2 (little optimized)"""


class Solution:
    def get_min_max(self, arr):
        n = len(arr)
        minEle = float('inf')
        maxEle = float('-inf')

        for i in range(n):
            minEle = min(arr[i], minEle)
            maxEle = max(arr[i], maxEle)

        return [minEle, maxEle]
