class Solution:
    def firstRepeated(self, arr):
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    return i + 1

        return -1
