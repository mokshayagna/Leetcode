class Solution:
    def removeStars(self, s: str) -> str:
        l = []
        for i in s:
            if len(l) ==0:
                l.append(i)
            else:
                if i == "*":
                    l.pop()
                else:
                    l.append(i)
        if len(l) != 0:
            return "".join(l)
        else:
            return ""