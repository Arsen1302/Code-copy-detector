class Solution:
    def solution_559_5_1(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        v, v1 = [], []
        
        def solution_559_5_2(tree):
            
            if not tree:
                return
            
            if tree.left is None and tree.right is None:
                v.append(tree.val)
            
            solution_559_5_2(tree.left)
            solution_559_5_2(tree.right)
        
        solution_559_5_2(root1)
        v1 = v
        v = []
        solution_559_5_2(root2)
        
        return v == v1