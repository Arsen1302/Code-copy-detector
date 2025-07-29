class Solution:
    def solution_1673_1_1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def solution_1673_1_2(n1, n2, level):
            if not n1:
                return
            
            if level % 2:
                n1.val, n2.val = n2.val, n1.val
                
            solution_1673_1_2(n1.left,  n2.right, level + 1)
            solution_1673_1_2(n1.right, n2.left,  level + 1)
            
        solution_1673_1_2(root.left, root.right, 1)       
        return root