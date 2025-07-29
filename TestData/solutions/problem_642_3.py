class Solution:
    def solution_642_3(self, nums: List[int]) -> int:
        
        for i in nums :
            if nums.count(i) == len(nums)/2 :
                return i