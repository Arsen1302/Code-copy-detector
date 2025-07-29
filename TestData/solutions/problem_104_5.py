class Solution:
    def solution_104_5(self, nums: List[int]) -> bool:
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = seen.get(nums[i], 0) + 1
        
        for k, v in seen.items():
            if v > 1:
                return True
        return False