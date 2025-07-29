class Solution:
    def solution_417_3_1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        
        def solution_417_3_2(root):
            if root == None:
                return TreeNode(val)
            if val < root.val:
                if root.left:
                    solution_417_3_2(root.left)
                else:
                    root.left = solution_417_3_2(root.left)
            else:
                if root.right:
                    solution_417_3_2(root.right)
                else:
                    root.right = solution_417_3_2(root.right)
        
        solution_417_3_2(root)
        return root