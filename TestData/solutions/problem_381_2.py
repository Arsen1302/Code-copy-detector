class Solution:
    def solution_381_2(self, nums: List[int]) -> TreeNode:
        if not nums: return # boundary condition 
        i = nums.index(max(nums))
        return TreeNode(nums[i], left=self.solution_381_2(nums[:i]), right=self.solution_381_2(nums[i+1:]))