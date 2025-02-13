class Solution:
    def findKthLargest(self, arr, k):
        arr.sort()
        arr.reverse()
        return arr[k - 1]


s = Solution()
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
