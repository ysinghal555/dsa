class Solution:
    def isArmstrong(self, num):
        n = len(str(num))

        res = 0
        temp = num

        while temp != 0:
            rem = temp % 10
            res = res + rem ** n
            temp = temp // 10

        if res == num:
            return True
        return False
