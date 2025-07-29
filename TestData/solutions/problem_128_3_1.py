class Solution:
    def solution_128_3_1(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return None
    
        res = []
        def solution_128_3_2(root, path):
            if not any([root.left, root.right]):
                res.append(path)
                
            solution_128_3_2(root.left, path + '->' + str(root.left.val)) if root.left else None
            solution_128_3_2(root.right, path + '->' + str(root.right.val)) if root.right else None
        
        solution_128_3_2(root, str(root.val))
        return res