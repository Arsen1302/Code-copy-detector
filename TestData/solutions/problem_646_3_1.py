class Solution:
    def solution_646_3_1(self, root: Optional[TreeNode]) -> bool:
        self.value=root.val
        self.flag=True
        def solution_646_3_2(node):
            if node is None:
                return True
            if node.val!=self.value:
                return False
            flag=solution_646_3_2(node.left) and solution_646_3_2(node.right)
            return flag
        return solution_646_3_2(root)