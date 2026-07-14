class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        
        suffix = [0]*n
        suffix[n-1] = nums[n-1]
        
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1] + nums[i]
        
        for i in range(n):
            left_sum = prefix[i] - nums[i]
            right_sum = suffix[i] - nums[i]

            if left_sum == right_sum:
                return i
            
        return -1
            