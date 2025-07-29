class Solution:
    def solution_1214_5(self, nums: List[int], limit: int, goal: int) -> int:
        
        return  (abs(goal - sum(nums)) + limit - 1) // limit