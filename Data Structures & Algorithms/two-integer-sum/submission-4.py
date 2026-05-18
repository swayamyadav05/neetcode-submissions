class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         seen = {}
         for i in range(len(nums)):
            k = target - nums[i]
            if k in seen and seen[k] != i:
                return [seen[k], i]
            seen[nums[i]] = i
            