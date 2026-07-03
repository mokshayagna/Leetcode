import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        if str1+str2 == str2+str1:
            a = math.gcd(len(str1),len(str2)) 
            res += str1[:a]
        return res