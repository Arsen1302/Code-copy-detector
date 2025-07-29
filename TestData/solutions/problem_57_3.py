class Solution:
    def solution_57_3(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        return [root.val] + self.solution_57_3(root.left) + self.solution_57_3(root.right)