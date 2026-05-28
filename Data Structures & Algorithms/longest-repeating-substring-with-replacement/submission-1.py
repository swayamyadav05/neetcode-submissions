class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        """
        "AAABABB"
             ^ ^
          

        charFreq = {"A": 1, "B": 3}
        windowLen = r - l + 1 = 4
        maxFreq = max(charFreq.values()) = 3
        windowLen - maxFreq = 1

        if windowLen - maxFreq <= k: 
            longest = max(longest, windowLen) = 5
            continue
        l += 1

        """
        

        longest = 0
        l = 0

        charFreq = {}
        for r in range(l, len(s)):
            charFreq[s[r]] = 1 + charFreq.get(s[r], 0)
            windowLen = r - l + 1
            maxFreq = max(charFreq.values())

            if windowLen - maxFreq <= k:
                longest = max(longest, windowLen)
                continue
            charFreq[s[l]] -= 1
            l += 1

        return longest
