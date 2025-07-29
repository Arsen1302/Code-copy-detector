class Solution:
    def solution_646_1_1(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        
        def solution_646_1_2(root):
            return root is None or (root.val == val and solution_646_1_2(root.left) and solution_646_1_2(root.right))
        
        return solution_646_1_2(root)