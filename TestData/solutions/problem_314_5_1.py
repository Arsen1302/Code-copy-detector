class Solution:
    def solution_314_5_1(self, root: Optional[TreeNode]) -> int:
        a = []
    
        def solution_314_5_2(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            
            solution_314_5_2(node.left)
            a.append(node.val)
            solution_314_5_2(node.right)
            
        solution_314_5_2(root)
        
        n = len(a)
        diff = float('inf')
        
        for i in range(1, n):
            diff = min(diff, a[i] - a[i - 1])
            
        return diff