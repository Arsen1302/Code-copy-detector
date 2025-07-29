class Solution:
    def solution_107_2(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, x in enumerate(nums): 
            if x in seen and i - seen[x] <= k: return True 
            seen[x] = i
        return False