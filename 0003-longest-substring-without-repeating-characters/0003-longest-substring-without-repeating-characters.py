class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        sub_string = ""
        h = {}
        max_len = 0
        while j < len(s):

            if s[j] not in h:
                sub_string += s[j]
                h[s[j]] = 1

                if len(sub_string) > max_len:
                    max_len = len(sub_string)

                j += 1

            else:
                del h[s[i]]
                sub_string = sub_string[1:]
                i += 1
        return max_len