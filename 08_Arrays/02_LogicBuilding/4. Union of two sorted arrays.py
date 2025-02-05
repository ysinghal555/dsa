"""Method 1"""


class Solution:
    def unionArray(self, a1, a2):
        res = set()
        n1 = len(a1)
        n2 = len(a2)

        for i in range(n1):
            res.add(a1[i])

        for i in range(n2):
            res.add(a2[i])

        res = list(res)
        res.sort()

        return res


"""Method 2"""


class Solution:
    def unionArray(self, a1, a2):
        n1 = len(a1)
        n2 = len(a2)
        res = []
        i = 0
        j = 0

        while i < n1 and j < n2:
            if a1[i] <= a2[j]:
                if len(res) == 0 or res[-1] != a1[i]:
                    res.append(a1[i])
                i += 1
            else:
                if len(res) == 0 or res[-1] != a2[j]:
                    res.append(a2[j])
                j += 1

        while i < n1:
            if len(res) == 0 or res[-1] != a1[i]:
                res.append(a1[i])
            i += 1

        while j < n2:
            if len(res) == 0 or res[-1] != a2[j]:
                res.append(a2[j])
            j += 1

        return res
