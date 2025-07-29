class Solution:
    def solution_925_4(self, nums: List[int], index: List[int]) -> List[int]:
        
        res=[]
        
        for i in range(len(nums)):
            res.insert(index[i],nums[i])