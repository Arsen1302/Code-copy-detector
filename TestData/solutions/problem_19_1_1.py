class Solution:
    def solution_19_1_1(self, inorder, postorder):
        inorderIndexDict = {ch : i for i, ch in enumerate(inorder)}
        self.rootIndex = len(postorder) - 1
        
        def solution_19_1_2(l, r):
            if l > r: return None
            
            root = TreeNode(postorder[self.rootIndex]) 
            self.rootIndex -= 1
            
            i = inorderIndexDict[root.val]
            
            # As we a approaching from end and all right side nodes of i in inorder are
            # from right sub-tree so first call solution_19_1_2 for right then left.
            root.right = solution_19_1_2(i+1, r)
            root.left =  solution_19_1_2(l, i-1)
            
            return root
        
        return solution_19_1_2(0, len(inorder)-1)
    
    
# Time: O(N)
# Space: O(1)