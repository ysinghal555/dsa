class Solution:
    def reverseArr(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

        return arr

    def rotateArray(self, arr, k):
        n = len(arr)
        arr = self.reverseArr(arr, 0, n - 1)
        arr = self.reverseArr(arr, 0, n - (k % n) - 1)
        arr = self.reverseArr(arr, n - (k % n), n - 1)

        return arr
