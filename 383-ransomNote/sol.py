class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for c in ransomNote:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1

        for c in magazine:
            if c in d:
                d[c] -= 1

        for _, key in enumerate(d):
            if d[key] > 0:
                return False

        return True
    
# O(n + m), where n is ransomeNote, m is magazine
# Count all charss in random and magazine and do some logic 