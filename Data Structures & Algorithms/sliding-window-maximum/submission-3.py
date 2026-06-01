class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k == 1:
            return nums
        
        res = []
        window = []

        for r in range(k):
            window.append(nums[r])

        maxi = max(window)
        res.append(maxi)

        l = 1
        while r - l + 1 < k:
            window.pop(0)
            r += 1
            if r < len(nums):
                window.append(nums[r])
                maxi = max(window)
                res.append(maxi)
                l += 1
        return res