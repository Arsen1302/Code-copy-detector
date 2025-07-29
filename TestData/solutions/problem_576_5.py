class Solution:
    def solution_576_5(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.solution_576_5(preorder[1: mid+1], inorder[:mid])
        root.right = self.solution_576_5(preorder[mid+1:], inorder[mid+1:])
        return root