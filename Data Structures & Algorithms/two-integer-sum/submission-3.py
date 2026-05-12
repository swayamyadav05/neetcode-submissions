class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            k = target - nums[i]
            if k in map and map[k] != i:
                return [map[k], i]
            map[nums[i]] = i
            