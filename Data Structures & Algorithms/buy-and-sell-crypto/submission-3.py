class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [7, 1, 5, 3, 6, 4]
         ^  ^  ^  ^  ^  ^
         l  r  r  r  r -r-
            ^ 
           -l- 

        res = 5
        """
        l, r = 0, 1
        res = 0

        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])
            r += 1
        return res

# TC = O(n)
# SC = O(1)