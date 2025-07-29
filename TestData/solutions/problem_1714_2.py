class Solution:
    def solution_1714_2(self, nums: List[int]) -> int:
        nums.sort()
        seen = set()
        for i in range(len(nums)//2): 
            seen.add((nums[i] + nums[~i])/2)
        return len(seen)