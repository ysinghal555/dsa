class Solution:
    def secondLargestElement(self, arr):
        n = len(arr)
        fmax = float('-inf')
        smax = float('-inf')

        for i in range(n):
            if arr[i] > fmax:
                smax = fmax
                fmax = arr[i]
            elif fmax > arr[i] > smax:
                smax = arr[i]

        return smax


s = Solution()
print(s.secondLargestElement([8, 8, 7, 6, 5]))
