class Solution:
    def solution_37_1_1(self):
        self.maxSum = float('-inf')
    def solution_37_1_2(self, root: TreeNode) -> int:
        def solution_37_1_3(root):
            if root:
                left = solution_37_1_3(root.left)
                right = solution_37_1_3(root.right)
                self.maxSum = max(self.maxSum,root.val, root.val + left, root.val + right, root.val + left + right)
                return max(root.val,root.val + left,root.val + right)
            else:
                return 0
        solution_37_1_3(root)
        return self.maxSum