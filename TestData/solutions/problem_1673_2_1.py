class Solution:
    def solution_1673_2_1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left:
            return root
        
        def solution_1673_2_2(node1, node2, rev):
            if rev:
                node1.val, node2.val = node2.val, node1.val
            
            if node1.left:
                solution_1673_2_2(node1.left, node2.right, not rev)
                solution_1673_2_2(node1.right, node2.left, not rev)
    
        solution_1673_2_2(root.left, root.right, True)
        return root