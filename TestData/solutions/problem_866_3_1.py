class Solution:
    def solution_866_3_1(self, root: TreeNode) -> int:
        ans = 0
        def solution_866_3_2(current: TreeNode, parent=-1, grandparent=-1):
            nonlocal ans
            if current is None:
                return 0
            if grandparent % 2 == 0:
                ans += current.val
            solution_866_3_2(current.left, current.val, parent)
            solution_866_3_2(current.right, current.val, parent)
        if root.left:
            solution_866_3_2(root.left, root.val)
        if root.right:
            solution_866_3_2(root.right, root.val)
        return ans