class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        highest = 0

        for i in gain:
            curr = curr + i
            highest = max(highest, curr)
        return highest