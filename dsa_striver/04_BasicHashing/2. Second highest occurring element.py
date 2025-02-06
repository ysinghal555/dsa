class Solution:
    def secondMostFrequentElement(self, arr):
        n = len(arr)
        hash_dict = {}

        for i in range(n):
            if arr[i] in hash_dict:
                hash_dict[arr[i]] += 1
            else:
                hash_dict[arr[i]] = 1

        tempArr = []

        for key, val in hash_dict.items():
            tempArr.append(val)

        n1 = len(tempArr)

        fmax = float('-inf')
        smax = float('-inf')

        for i in range(n1):
            if tempArr[i] > fmax:
                smax = fmax
                fmax = tempArr[i]
            elif fmax > tempArr[i] > smax:
                smax = tempArr[i]
