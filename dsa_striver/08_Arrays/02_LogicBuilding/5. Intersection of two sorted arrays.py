class Solution:
    def intersectionArray(self, a1, a2):
        n1 = len(a1)
        n2 = len(a2)
        i = 0
        j = 0
        res = []

        while i < n1 and j < n2:
            if a1[i] == a2[j]:
                res.append(a1[i])
                i += 1
                j += 1
            elif a1[i] > a2[j]:
                j += 1
            else:
                i += 1

        return res
