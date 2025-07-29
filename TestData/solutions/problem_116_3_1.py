class Solution:
    def solution_116_3_1(self, root: Optional[TreeNode], k: int) -> int:
        
        l=[]
        
        
        def solution_116_3_2(node):
            if not node:
                return 
            l.append(node.val)
            solution_116_3_2(node.left)
            solution_116_3_2(node.right)
        
        
        solution_116_3_2(root)
        l.sort()
        l=list(set(l))
        return l[k-1]