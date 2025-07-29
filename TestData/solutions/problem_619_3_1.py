class Solution:
    def solution_619_3_1(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0

        def solution_619_3_2(node: Optional[TreeNode]):
            nonlocal ans
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if node.left and node.val > low:
                    solution_619_3_2(node.left)
                if node.right and node.val < high:
                    solution_619_3_2(node.right)

        solution_619_3_2(root)
        return ans