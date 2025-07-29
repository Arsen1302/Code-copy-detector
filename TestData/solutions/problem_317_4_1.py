class Solution:
    def solution_317_4_1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def solution_317_4_2(root, sm):
            if root is None: return sm
            right = solution_317_4_2(root.right, sm)
            root.val += right
            left = solution_317_4_2(root.left, root.val)
            return left
        solution_317_4_2(root, 0)
        return root