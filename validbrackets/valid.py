class Solution:
    def isValid(self, s: str) -> bool:
        h = {'{':'}', '[': ']', '(':')'}
        stac = []
        for c in s:
            if c in h.keys():
                stac.append(c)
            else:
                # empty or
                # brackets dont match
                if not stac or h[stac.pop()] != c:
                    return False

        return len(stac) == 0


# Time complexitey: O(N), only loops through s elements once. only appends one type of bracket.
#  