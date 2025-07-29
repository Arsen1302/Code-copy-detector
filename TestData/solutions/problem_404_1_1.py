class Solution:
    def solution_404_1_1(self, root: TreeNode) -> int:
        
        def solution_404_1_2(node): 
            """Return longest univalue branch and longest univalue path (post-order traversal)."""
            if not node: return 0, 0
            (lx, llup), (rx, rlup) = solution_404_1_2(node.left), solution_404_1_2(node.right) 
            if not node.left or node.left.val != node.val: lx = 0
            if not node.right or node.right.val != node.val: rx = 0 
            return 1 + max(lx, rx), max(llup, rlup, 1 + lx + rx)
        
        return max(0, solution_404_1_2(root)[-1]-1)