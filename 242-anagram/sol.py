class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1

        for c in t:
            if c in d:
                d[c] -= 1
            else:
                d[c] = 1
        
        for _, val in enumerate(d):
            if d[val] != 0:
                return False

        return True

        