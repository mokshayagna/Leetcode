class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        c = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            a = x % 10  
            c = c*10 + a
            x = x //10
        c = sign * c
        if c < -2**31 or c > 2 **31 -1:
            return 0
        return c