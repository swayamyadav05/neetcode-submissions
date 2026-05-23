class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        [1,7,2,5,4,7,3,6]
         ^ ^ ^ ^ ^ ^ ^ ^
        [0 1 2 3 4 5 6 7]

        containers: 
        1. [1,7] = min(1,7) * (1-0) = 1
        2. [1, 6] = min(1,6) * (7-0) = 1 * 7 = 7
        ...
        ...
        3. [7, 6] = min(7,6) * (7-1) = 6 * 6 = 36

        distance matters and only if the containers size will be [1,1,1,7, 7,1]

        [1,7,2,5,4,7,3,6]
         ^             ^
         l             r

        container contains water = 1 * 7 = 7
        we check if nums[l] >= nums[r]: r -= 1 or l += 1
           ans = 7
        [1,7,2,5,4,7,3,6]
           ^ ^
        
        water = 6 * 6 = 36
        ans = max(ans, water) = 36
        
        water = 2 * 1 = 2
        """

        ans = 0
        l, r = 0, len(heights) - 1

        while l < r:
            waterCon = min(heights[l], heights[r]) * (r - l)
            ans = max(ans, waterCon)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        
        return ans

# TC = O(n)
# SC = O(1)