class Solution:
    def solution_381_1(self, nums: List[int]) -> TreeNode:
        
        # base case
        if not nums:
            return None
        
        max_val = max(nums)
        max_idx = nums.index(max_val)
        root = TreeNode(max_val)
        
        root.left = self.solution_381_1(nums[:max_idx])
        root.right = self.solution_381_1(nums[max_idx+1:])
        
        return root