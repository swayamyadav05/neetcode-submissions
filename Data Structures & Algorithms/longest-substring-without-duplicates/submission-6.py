class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMp = {}
        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] in charMp:
                left = max(charMp[s[right]] + 1, left)
            charMp[s[right]] = right
            res = max(res, right - left + 1)
        return res

# TC = O(n)
# SC = O(m)