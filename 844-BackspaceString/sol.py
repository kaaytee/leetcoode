class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s_1 = []

        for c in s:
            if c == "#" and not s_1:
                continue
            elif c == "#":
                s_1.pop()
            else:
                s_1.append(c)

        s_2 = []
        for c in t:
            if c == "#" and not s_2 :
                continue
            elif c == "#":
                s_2.pop()
            else:
                s_2.append(c)


        return s_2 == s_1
    
    
# O(N + m) time complexiety
# O(N + m) space complexity -> can O(1) sspace with 2 pointer mayb