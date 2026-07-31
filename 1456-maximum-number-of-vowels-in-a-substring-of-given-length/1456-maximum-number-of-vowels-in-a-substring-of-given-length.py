class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        max_count = 0
        vowels = "aeiou"
        sub_string = s[:k]
        for ch in sub_string:
            if ch.lower() in vowels:
                count += 1
        max_count = count
        i = 0
        j = k
        while j < len(s):
            if s[i].lower() in vowels:
                count -= 1
            if s[j].lower() in vowels:
                count += 1
            i += 1
            j += 1
            max_count = max(max_count,count)
        return max_count