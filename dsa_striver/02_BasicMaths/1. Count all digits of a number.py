"""Method 1"""


class Solution:
    def countDigit(self, num):
        return len(str(num))


"""Method 2"""


class Solution:
    def countDigit(self, num):

        if num == 0:
            return 1

        cnt = 0

        while num != 0:
            num = num // 10
            cnt += 1

        return cnt
