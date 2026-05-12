class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = i
            k = target - nums[i]
            
            if k in map and map[k] != i:
                return [map[k], i]