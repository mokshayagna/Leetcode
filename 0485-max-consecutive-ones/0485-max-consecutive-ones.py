class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        j = 0
        count = 0
        while i < len(nums) and j < len(nums):
            if nums[j] == 1:
                j += 1
            elif nums[j] == 0:
                count = max(count,(j - i))
                i = j + 1
                j = j + 1
        count = max(count,j - i)
        return count