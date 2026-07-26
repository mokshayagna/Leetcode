class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        res = ""
        h = {}
        for char in magazine:
            if char in h:
                h[char] += 1
            else:
                h[char] = 1
        for i in ransomNote:
            if i not in h:
                return False
            else:
                res += i
                h[i] -= 1
            if res == ransomNote:
                return True
            if h[i] == 0:
                del h[i]
