"""Method 1"""

# class Solution:
#     # Function to sort an array of 0s, 1s, and 2s
#     def sort012(self, arr):
#         n = len(arr)
#         arrOf0 = []
#         arrOf1 = []
#         arrOf2 = []
#
#         for i in range(n):
#             if arr[i] == 0:
#                 arrOf0.append(arr[i])
#             elif arr[i] == 1:
#                 arrOf1.append(arr[i])
#             else:
#                 arrOf2.append(arr[i])
#
#         j = 0
#         for i in range(len(arrOf0)):
#             arr[j] = arrOf0[i]
#             j += 1
#
#         for i in range(len(arrOf1)):
#             arr[j] = arrOf1[i]
#             j += 1
#
#         for i in range(len(arrOf2)):
#             arr[j] = arrOf2[i]
#             j += 1
#
#         return arr


"""Method 2"""


class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        n = len(arr)
        low = 0
        mid = 0
        high = n - 1

        for i in range(n):
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                mid += 1
                low += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr


s = Solution()
print(s.sort012([0, 2, 1, 2, 0, 2]))
