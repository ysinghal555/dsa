class Solution:
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False

        tempStr = s + s
        if goal in tempStr:
            return True

        return False
