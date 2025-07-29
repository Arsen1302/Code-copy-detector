class Solution:
    def solution_18_4_1(self, preorder, inorder):
        inorderIndexDict = {ch : i for i, ch in enumerate(inorder)}
        self.rootIndex = 0
        
        def solution_18_4_2(l, r):
            if l > r: return None
            
            root = TreeNode(preorder[self.rootIndex])
            self.rootIndex += 1
            
            i = inorderIndexDict[root.val]
            
            root.left = solution_18_4_2(l, i-1)
            root.right = solution_18_4_2(i+1, r)
            
            return root
        
        return solution_18_4_2(0, len(inorder)-1)
    
    
# Time: O(N)
# Space: O(1)