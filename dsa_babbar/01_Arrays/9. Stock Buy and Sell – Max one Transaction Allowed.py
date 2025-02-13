class Solution:
    def maximumProfit(self, arr):
        n = len(arr)
        buy = arr[0]
        profit = 0

        for i in range(1, n):
            if arr[i] < buy:
                buy = arr[i]

            profit = max(profit, arr[i] - buy)

        return profit
