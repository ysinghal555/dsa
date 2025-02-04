class Solution:
    def frequencySort(self, s):
        hashdict = {}

        for i in s:
            if i in hashdict:
                hashdict[i] += 1
            else:
                hashdict[i] = 1

        """
        -x[1] → Sort by frequency in descending order.
        x[0] → Sort alphabetically if frequencies are the same.
        """

        sortedDict = dict(sorted(hashdict.items(), key=lambda x: (-x[1], x[0])))
        ans = []

        for key, val in sortedDict.items():
            ans.append(key)

        return ans
