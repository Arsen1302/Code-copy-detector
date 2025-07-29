class Solution:
    def solution_576_4(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        index = postorder.index(preorder[1])
        root.left = self.solution_576_4(preorder[1:index+2], postorder[:index+1])
        root.right = self.solution_576_4(preorder[index+2:], postorder[index+1:-1])
        return root