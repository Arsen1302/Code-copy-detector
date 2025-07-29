class Solution:
    def solution_404_2_1(self, root: TreeNode) -> int:
        
        def solution_404_2_2(node): 
            """Return longest univalue branch and longest univalue path (post-order traversal)."""
            nonlocal ans 
            if not node: return 0
            lx, rx = solution_404_2_2(node.left), solution_404_2_2(node.right) 
            if not node.left or node.left.val != node.val: lx = 0
            if not node.right or node.right.val != node.val: rx = 0 
            ans = max(ans, 1 + lx + rx)
            return 1 + max(lx, rx)
        
        ans = 0
        solution_404_2_2(root)
        return max(0, ans-1)