class Solution:
    def mostFrequentElement(self, nums):
        hash_dict = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in hash_dict:
                hash_dict[nums[i]] += 1
            else:
                hash_dict[nums[i]] = 1

        minElement = float('inf')
        maxVal = 0

        for key, val in hash_dict.items():
            if val > maxVal:
                maxVal = val
                minElement = key
            elif val == maxVal:
                minElement = min(minElement, key)

        return minElement
