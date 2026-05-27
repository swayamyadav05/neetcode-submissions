class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        [1, 7, 2, 5, 4, 7, 3, 6]
            ^                 ^

        water = (r - l) * min(l, r) = 7 -> 36  
        """

        ans = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            ans = max(ans, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return ans