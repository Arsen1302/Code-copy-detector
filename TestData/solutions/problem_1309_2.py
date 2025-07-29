class Solution:
    def solution_1309_2(self, nums: List[int]) -> List[int]:
        # time:O(N) space:O(N)
        
         ans=[0]*len(nums)
         for i in range(len(nums)):
             ans[i] = nums[nums[i]]
         return ans