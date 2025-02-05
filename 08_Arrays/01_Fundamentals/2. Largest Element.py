class Solution:
    def largestElement(self, nums):
        maxEle = float('-inf')

        for i in nums:
            maxEle = max(i, maxEle)

        return maxEle
