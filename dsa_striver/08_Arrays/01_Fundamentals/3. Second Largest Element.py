class Solution:
    def secondLargestElement(self, arr):
        if len(arr) < 2:
            return -1

        fmax = float('-inf')
        smax = float('-inf')

        for num in arr:
            if num > fmax:
                smax = fmax
                fmax = num
            elif fmax > num > smax:
                smax = num

        return smax if smax != float('-inf') else -1
