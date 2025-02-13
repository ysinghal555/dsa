class Solution:
    def segregateElements(self, arr):
        n = len(arr)
        negArr = []
        posArr = []

        for i in range(n):
            if arr[i] >= 0:
                posArr.append(arr[i])
            else:
                negArr.append(arr[i])

        j = 0
        for i in range(len(posArr)):
            arr[j] = posArr[i]
            j += 1

        for i in range(len(negArr)):
            arr[j] = negArr[i]
            j += 1

        return arr
