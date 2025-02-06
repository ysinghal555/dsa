# Min element in the starting

"""
The selection sort algorithm sorts an array by repeatedly finding the minimum element from the unsorted part and
putting it at the beginning. The largest element will end up at the last index of the array.
"""


class Solution:
    def selectionSort(self, arr):
        n = len(arr)

        for i in range(n):
            minIndex = i
            for j in range(i + 1, n):
                if arr[j] < arr[minIndex]:
                    minIndex = j

            if minIndex != i:
                arr[i], arr[minIndex] = arr[minIndex], arr[i]

        return arr
