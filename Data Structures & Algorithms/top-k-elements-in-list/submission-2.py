class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resMap = {}
        res = []
        for i in range(len(nums)):
            resMap[nums[i]] = 1 + resMap.get(nums[i], 0)
        for key, value in resMap.items():
            res.append([value, key])
        res.sort()

        result = []
        while len(result) < k:
            result.append(res.pop()[1])
        return result