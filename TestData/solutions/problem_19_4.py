class Solution:
    def solution_19_4(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return
        
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        root.left = self.solution_19_4(inorder[:mid], postorder[:mid])
        root.right = self.solution_19_4(inorder[mid+1:], postorder[mid:-1])
        return root