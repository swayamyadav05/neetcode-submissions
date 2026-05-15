class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0
        res = []

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                prod *= num

        for num in nums:
            if zeros > 1:
                res.append(0)
            elif zeros == 1:
                res.append(prod if num == 0 else 0)
            else:
                res.append(prod // num)
        return res
             