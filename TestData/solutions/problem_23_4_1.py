class Solution:

    def solution_23_4_1(self, root: TreeNode) -> bool:
        return not root.left and not root.right

    def solution_23_4_2(self, root: TreeNode) -> bool:
        if not root:
            return True

        if self.solution_23_4_1(root):
            root.height = 1
            return True
        elif not root.left and root.right:
            if self.solution_23_4_1(root.right):
                root.height = 2
                return True
            return False
        elif root.left and not root.right:
            if self.solution_23_4_1(root.left):
                root.height = 2
                return True
            return False
        elif self.solution_23_4_2(root.left) and self.solution_23_4_2(root.right):
            if abs(root.left.height - root.right.height) <= 1:
                root.height = max(root.left.height, root.right.height) + 1
                return True
            return False
        return False