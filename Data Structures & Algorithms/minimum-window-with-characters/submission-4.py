class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): 
            return ""

        tCount, sCount = {}, {}
        for c in t: 
            tCount[c] = 1 + tCount.get(c, 0)
 
        need, have = len(tCount), 0 

        res = [-1, -1]
        resLen = float("inf")

        l = 0

        for r in range(l, len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)

            if s[r] in tCount and sCount[s[r]] == tCount[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]

                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1

        return s[res[0] : res[1] + 1] if resLen != float("inf") else ""
# TC = O(n)
# SC = O(1)