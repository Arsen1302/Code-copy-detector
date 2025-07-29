class Solution:
    def solution_19_5_1(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def solution_19_5_2(inorder,postorder,n):
            if not inorder or not postorder:
                return None
            root = TreeNode(postorder[-1])
            mid = inorder.index(postorder[-1])
            root.left = solution_19_5_2(inorder[:mid],postorder[:mid],mid)
            root.right = solution_19_5_2(inorder[mid+1:],postorder[mid:n-1],n-mid-1)
            return root
        return solution_19_5_2(inorder,postorder,len(inorder))