import math


class Solution:
    def isomorphicString(self, s1, s2):
        if len(s1) != len(s2):
            return False
        n = len(s1)
        s1_to_s2 = {}
        s2_to_s1 = {}

        for i in range(n):
            char1 = s1[i]
            char2 = s2[i]

            if char1 in s1_to_s2:
                if s1_to_s2[char1] != char2:
                    return False
            else:
                s1_to_s2[char1] = char2

            if char2 in s2_to_s1:
                if s2_to_s1[char2] != char1:
                    return False
            else:
                s2_to_s1[char2] = char1

        return True


s = Solution()
print(s.isomorphicString("aabcffzzzzz", "ddbiaaaaaaa"))
