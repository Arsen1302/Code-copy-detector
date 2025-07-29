class Solution:
    def solution_925_1(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(nums)):
            ans.insert(index[i] , nums[i])
        
        return ans