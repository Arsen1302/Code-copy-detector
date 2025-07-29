class Solution:
    def solution_961_5(self, nums: List[int], k: int) -> bool:
        ii = -inf
        for i, x in enumerate(nums): 
            if x: 
                if i - ii <= k: return False 
                ii = i 
        return True