class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l1 = []
        l2 = []
        for ch in s:
            if ch == "#":
                if l1:
                    l1.pop()
            else:
                l1.append(ch)
        for ch in t:
            if ch == "#":
                if l2:
                    l2.pop()
            else:
                l2.append(ch)
        if l1 == l2:
            return True
        else:
            return False