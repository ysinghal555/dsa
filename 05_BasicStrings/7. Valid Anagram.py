class Solution:
    def anagramStrings(self, s, t):
        dict1 = {}

        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        for i in t:
            if i in dict1:
                dict1[i] -= 1
            else:
                return False

        for key, val in dict1.items():
            if val != 0:
                return False

        return True
