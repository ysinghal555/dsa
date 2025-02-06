"""Method 1"""


class Solution:
    def palindromeCheck(self, s):
        if s[::] == s[::-1]:
            return True

        return False


"""Method 2"""


class Solution:
    def palindromeCheck(self, s):
        n = len(s)
        i = 0
        j = n - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True
