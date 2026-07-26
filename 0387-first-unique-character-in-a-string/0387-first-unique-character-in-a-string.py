class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = {}
        for i in range(len(s)):
            if s[i] not in h:
                h[s[i]] = [1,i]
            else:
                h[s[i]][0] += 1
        for char,data in h.items():
            if data[0] == 1:
                return data[1]
                break
        return -1
