class Solution:
    def sumOfFirstAndLast(self, nums):
        n = len(nums)
        if n == 0:
            return -1

        return nums[0] + nums[-1]