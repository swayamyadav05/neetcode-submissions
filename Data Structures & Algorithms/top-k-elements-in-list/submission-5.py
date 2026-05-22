class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        temp = []

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        for key, value in count.items():
            temp.append([value, key])
        temp.sort()

        result = []
        while len(result) < k:
            result.append(temp.pop()[1])
        
        return result