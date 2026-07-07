class Solution:
    def sumAndMultiply(self, n: int) -> int:
        l = []
        for digit in str(n):
            if digit != "0":
                l.append(digit)
            x = "".join(l)
        if x == "":
            return 0
        sum = 0
        for i in x:
            sum = sum + int(i)
        return (sum * int(x))