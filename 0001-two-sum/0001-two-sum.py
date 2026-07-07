from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            sec = target - nums[i]
            if sec in hash:
                return(hash[sec],i)
            else:
                hash[nums[i]] = i