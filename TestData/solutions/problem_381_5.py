class Solution:
    def solution_381_5(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        _max = max(nums)
        _max_i = nums.index(_max)
        
        root = TreeNode(_max)
        root.left = self.solution_381_5(nums[:_max_i])
        root.right = self.solution_381_5(nums[_max_i+1:])
        
        return root