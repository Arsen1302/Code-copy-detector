class Solution:
    def solution_404_3_1(self, root: Optional[TreeNode]) -> int:
        
        max_len = 0
        
        def solution_404_3_2(node):
            
            nonlocal max_len
            
            if not node.left and not node.right:
            # if not node:
                return 0
            
            wide = 0
            current_depth = 0
            
            if node.left:
                left_depth = solution_404_3_2(node.left)
                if node.left.val == node.val:
                    wide += 1 + left_depth
                    current_depth = max(current_depth, 1+left_depth)
                    
            if node.right:
                right_depth = solution_404_3_2(node.right)
                if node.right.val == node.val:
                    wide += 1 + right_depth
                    current_depth = max(current_depth, 1+right_depth)
                
            max_len = max(max_len, wide, current_depth)
            
            return current_depth
        
        if root:
            solution_404_3_2(root)
            
        return max_len