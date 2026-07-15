class Solution:
    def subarraySum(self, arr: List[int], tar: int) -> int:
        n = len(arr)
        prefix = [0]*n
        prefix[0] = arr[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + arr[i]
        
        count = 0
        freq = {}
        for i in range(n):
            if prefix[i] == tar:
                count += 1
            val = prefix[i] - tar
            if val in freq:
                count += freq[val]
            if prefix[i] not in freq:
                freq[prefix[i]] = 0
            freq[prefix[i]] += 1
        return count