class Solution:
    def solution_116_2_1(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []
        
        def solution_116_2_2(node):
            if (not node or (len(res) >= k)):
                return
            
            solution_116_2_2(node.left)
            res.append(node.val)
            solution_116_2_2(node.right)
            
        solution_116_2_2(root)
        
        return res[k - 1]