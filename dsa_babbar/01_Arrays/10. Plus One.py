class Solution:
    def plusOne(self, arr: List[int]) -> List[int]:
        n = len(arr)
        num = ''
        for i in range(n):
            num += str(arr[i])

        num = str(int(num) + 1)
        res = [int(i) for i in num]
        return res
