class Solution:
    # Function to return the position of the first repeating element.
    def firstRepeated(self, arr):
        n = len(arr)
        res = {}
        for i in range(n):
            if arr[i] in res:
                return res[arr[i]] + 1
            res[arr[i]] = i

        return -1


s = Solution()
# print(s.firstRepeated([7, 4, 0, 9, 4, 8, 8, 2, 4, 5, 5, 1]))
print(s.firstRepeated([1, 5, 3, 4, 3, 5, 6]))
