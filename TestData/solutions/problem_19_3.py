class Solution:
    def solution_19_3(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.solution_19_3(preorder[1: mid+1], inorder[:mid])
        root.right = self.solution_19_3(preorder[mid+1:], inorder[mid+1:])
        return root