"""Method 1"""


class Solution:
    def longestCommonPrefix(self, arr):
        first = arr[0]
        ans = ""

        for i in range(len(arr[0])):
            substr = first[:i]
            isSame = True
            for j in arr:
                if j[:i] != substr:
                    isSame = False
                    break

            if isSame:
                ans = substr

        return ans


"""Method 2"""


class Solution:
    def longestCommonPrefix(self, arr):
        n = len(arr)
        arr.sort()
        first = arr[0]
        last = arr[n - 1]
        ans = ""
        for i in range(len(first)):
            if first[:i] != last[:i]:
                break
            ans = first[:i]

        return ans
