class Solution:
    def solution_27_4_1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        res=[]
        # Functtion to return the preorder Traversal
        def solution_27_4_2(root):
            if not root:
                return
            res.append(root.val)
        
            solution_27_4_2(root.left)
            solution_27_4_2(root.right)
            
        solution_27_4_2(root)
        
        #iterating through the res list to create a flattened list
        
        for i in range(1,len(res)):
            temp = TreeNode(res[i])
            root.right = temp
            root.left = None
            root= root.right