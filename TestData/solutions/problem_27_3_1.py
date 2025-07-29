class Solution:
    def solution_27_3_1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        #writing the function to solution_27_3_1 the binary tree
        
        def solution_27_3_2(root):
            """
            param type root: TreeNode
                  rtype root
            """
            if not root:
                return
            
            left_end = solution_27_3_2(root.left)
            right_end = solution_27_3_2(root.right)
            
            if left_end:
                
                left_end.right = root.right
                root.right = root.left
                root.left = None
                
            end_pointer = right_end or left_end or root
            
            return end_pointer
        
        solution_27_3_2(root)