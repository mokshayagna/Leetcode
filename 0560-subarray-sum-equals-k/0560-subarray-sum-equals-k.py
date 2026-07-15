class Solution:
    def subarraySum(self, arr: List[int], tar: int) -> int:
        prefix = 0
        count = 0
        freq = {}
        for i in range(len(arr)):
            prefix = prefix + arr[i]

            val = prefix - tar
            if val in freq:
                count += freq[val]
            if prefix not in freq:
                freq[prefix] = 0
            freq[prefix] += 1

            if prefix == tar:
                count += 1
        return count