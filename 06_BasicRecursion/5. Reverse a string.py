"""Method 1 (Not using Recursion)"""


class Solution:
    def reverseString(self, arr):
        n = len(arr)
        i = 0
        j = n - 1

        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

        return arr


"""Method 2 (Using Recursion)"""


class Solution:
    def reverseStringRecur(self, s, i, n):
        if i >= n // 2:
            return s

        s[i], s[n - i - 1] = s[n - i - 1], s[i]

        return self.reverseStringRecur(s, i + 1, n)

    def reverseString(self, s):
        return self.reverseStringRecur(s, 0, len(s))
