class Solution:
    def solution_925_5(self, nums: List[int], index: List[int]) -> List[int]:
        
        list = []
        
        [list.insert(ind, num) for num, ind in zip(nums, index)]
        
        return list