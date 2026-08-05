class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        max_res = nums[0]
        res = 0
        while j < len(nums):
            res += nums[j]
            max_res = max(max_res,res)
            if res < 0:
                res = 0
                i = j + 1
            j += 1
        return max_res