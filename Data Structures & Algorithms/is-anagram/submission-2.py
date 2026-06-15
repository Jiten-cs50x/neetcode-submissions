class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            x = s[i]
            if x in s and t:
                y = s.count(x) - t.count(x)
            if y != 0:
                return False
        
        return True