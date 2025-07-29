class Solution:
    def solution_19_2(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        index = postorder.index(preorder[1])
        root.left = self.solution_19_2(preorder[1:index+2], postorder[:index+1])
        root.right = self.solution_19_2(preorder[index+2:], postorder[index+1:-1])
        return root