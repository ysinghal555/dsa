class Solution:
    def reverse(self, arr, n):
        i = 0
        j = n - 1

        while i <= j:
            arr[i], arr[j] = arr[j], arr[i]

            i += 1
            j -= 1

        return arr
