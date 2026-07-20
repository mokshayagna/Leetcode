import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = nums[0]
        mx = nums[0]
        for num in nums:
            if num > mx:
                mx = num
            elif num < mn:
                mn = num
        res = math.gcd(mx,mn)
        return res