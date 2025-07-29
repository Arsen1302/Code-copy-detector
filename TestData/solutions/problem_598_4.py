class Solution:
    def solution_598_4(self, nums: List[int]) -> int:
        a = list(accumulate(nums, max)) 
        b = list(accumulate(nums[::-1], min))[::-1]
        for i in range(1, len(nums)):
            if a[i-1] <= b[i]: 
                return i