class Solution:
    def solution_1649_5_1(self, root: Optional[TreeNode], start: int) -> int:
        def solution_1649_5_2(root):
            if root is None:
                return None, 0
            
            node_l, l = solution_1649_5_2(root.left)
            node_r, r = solution_1649_5_2(root.right)
            
            if root.val == start:
                return 0, max(l, r)
            
            if node_l is not None:
                return node_l + 1, max(node_l + 1, l, node_l + 1 + r)
            
            if node_r is not None:
                return node_r + 1, max(node_r + 1, r, node_r + 1 + l)
            
            return None, max(l, r) + 1
        
        _, ans = solution_1649_5_2(root)
        return ans