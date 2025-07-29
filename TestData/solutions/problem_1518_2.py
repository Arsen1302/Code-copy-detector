class Solution:
    def solution_1518_2(self, nums: List[int]) -> bool:      
        return not reduce(lambda x,elem: x ^ {elem}, nums, set())