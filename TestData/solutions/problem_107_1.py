class Solution:
    def solution_107_1(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen: return True 
            seen.add(x)
        return False