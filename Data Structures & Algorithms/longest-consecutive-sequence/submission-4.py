class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0 
        if len(nums) == 1: return 1
        
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

# TC = O(n)
# SC = O(n)