class Solution:
    def isValid(self, stack: str) -> bool:
        s = []
        for i in stack:
            if i == "(" or i == "[" or i == "{":
                s.append(i)
            else:
                if len(s) == 0:
                    return False
                if i == ")" and s[-1] == "(":
                    s.pop()
                elif i == "}" and s[-1] == "{":
                    s.pop()
                elif i == "]" and s[-1] == "[":
                    s.pop()
                else:
                    return False
        if len(s) == 0:
            return True
        else:
            return False