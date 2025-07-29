class Solution:
    def solution_18_5(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
		# This gives the root data
        rootData = preorder[0]
        root = TreeNode(rootData)
        rootIdx = -1
        for i in range(len(inorder)):
            if rootData == inorder[i]:
                rootIdx = i
                break
                
        if rootIdx == -1:
            return None
        # This gives the leftInorder
        leftInorder = inorder[:rootIdx]
		#This gives the rightInorder
        rightInorder = inorder[rootIdx+1:]
        
        lenLeftSubTree = len(leftInorder)
        
        leftPreorder = preorder[1:lenLeftSubTree+1]
        rightPreorder = preorder[lenLeftSubTree+1:]
        
		# Recursion will build the tree 
        leftChild = self.solution_18_5(leftPreorder, leftInorder)
        rightChild = self.solution_18_5(rightPreorder, rightInorder)
        
		# Making connnections of the tree
        root.left = leftChild
        root.right = rightChild
        
        return root