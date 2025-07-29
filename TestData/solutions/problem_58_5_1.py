class Solution:
    def solution_58_5_1(self):
        self.postOrder = []
    def solution_58_5_2(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        if root:
            self.solution_58_5_2(root.left)
            self.solution_58_5_2(root.right)
            self.postOrder.append(root.val)
        return self.postOrder