class Solution:
    def isSortedRecur(self, arr, n, i, prev):
        if i == n - 1:
            return True
        if arr[i] < prev:
            return False

        prev = arr[i]

        return self.isSortedRecur(arr, n, i + 1, prev)

    def isSorted(self, arr):
        return self.isSortedRecur(arr, len(arr), 0, float('-inf'))


s = Solution()
arr = [1, 2, 3, 4, 5]
print(s.isSorted(arr))
