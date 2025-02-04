class Solution:
    def reverseArrayRecur(self, arr, i, n):
        if i >= n // 2:
            return arr

        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
        return self.reverseArrayRecur(arr, i + 1, n)

    def reverseArray(self, arr):
        return self.reverseArrayRecur(arr, 0, len(arr))
