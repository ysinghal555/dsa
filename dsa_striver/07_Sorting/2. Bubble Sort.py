# By doing adjacent swaps we need to send maz element to the end,

"""
The bubble sort algorithm sorts an array by repeatedly swapping adjacent elements if they are in the wrong order.
The largest elements "bubble" to the end of the array with each pass.
"""


class Solution:
    def bubbleSort(self, arr):
        n = len(arr)

        for i in range(n):
            isSwapped = False
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    isSwapped = True

            if not isSwapped:
                break

        return arr
