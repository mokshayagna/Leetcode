class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        j = len(s) - 1
        count = 0
        while j >= 0 and s[j] != " ":
            count += 1
            j -= 1
        return count