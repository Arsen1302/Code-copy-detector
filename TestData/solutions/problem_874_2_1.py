class Solution:
    def solution_874_2_1(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def solution_874_2_2(root):
            if root is None:
                return True
            left, right = solution_874_2_2(root.left), solution_874_2_2(root.right)
            if left:
                root.left = None
            if right:
                root.right = None
            
            return left and right and root.val == target
        
        return root if not solution_874_2_2(root) else None