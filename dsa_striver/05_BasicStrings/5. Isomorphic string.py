class Solution:
    def isomorphicString(self, s1, s2):
        if len(s1) != len(s2):
            return False

        n = len(s1)
        hashdict = {}

        for i in range(n):
            if s1[i] in hashdict:
                if hashdict[s1[i]] != s2[i]:
                    return False
            else:
                hashdict[s1[i]] = s2[i]

        return True

s = Solution()
print(s.isomorphicString("aabcffzzzzz", "ddbiaaaaaaa"))