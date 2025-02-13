class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            temp = str(num)
            sumNum = 0
            for i in temp:
                sumNum += int(i)

            num = sumNum

        return num
