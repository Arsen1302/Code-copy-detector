class Solution:
    def solution_1397_2_1(self, nums: List[int]) -> int:
        
        def solution_1397_2_2(i,val):
            if maxBit == val : return 1<<(len(nums)-i)
            if i == len(nums): return 0
            return solution_1397_2_2(i+1,val|nums[i]) + solution_1397_2_2(i+1,val)
        maxBit = 0
        for i in nums: maxBit |= i
        return solution_1397_2_2(0,0)