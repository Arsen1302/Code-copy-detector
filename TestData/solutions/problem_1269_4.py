class Solution:
    def solution_1269_4(self, nums: List[int]) -> int:
        sumXor = 0
        for i in nums:
            sumXor |= i
        return sumXor * 2 ** (len(nums)-1)