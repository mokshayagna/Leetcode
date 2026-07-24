class Solution:
    def myAtoi(self, a: str) -> int:
        a = a.lstrip()

        sign = 1
        i = 0

        if i < len(a) and a[i] == "-":
            sign = -1
            i += 1
        elif i < len(a) and a[i] == "+":
            sign = 1
            i += 1
        if i < len(a) and not a[i].isdigit():
            return 0
        num = 0
        while i < len(a) and a[i].isdigit():
            digit = int(a[i])
            num = num * 10 + digit
            i += 1
        num = num * sign
        if num < -2 ** 31:
            return -2 ** 31
        
        elif num > 2 ** 31 -1:
            return 2 ** 31 -1

        return num
            