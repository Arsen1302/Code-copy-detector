class Solution:
    def solution_21_3(self, nums: List[int]) -> TreeNode:
        # base case
        if not nums: return None
        
        # getting the mid
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        
        # left node is given the responsibility till mid, 
        # but not including mid
        node.left = self.solution_21_3(nums[:mid])
        # right node is given the responsibility from mid+1 
        # till the end
        node.right = self.solution_21_3(nums[mid+1:])
        return node