class Solution:
    def solution_1562_4_1(self, root: Optional[TreeNode]) -> int:
        count = 0

        def solution_1562_4_2(node: TreeNode) -> tuple:
            nonlocal count
            if not node:
                return 0, 0
            sum_left, count_left = solution_1562_4_2(node.left)
            sum_right, count_right = solution_1562_4_2(node.right)
            sum_total = sum_left + sum_right + node.val
            count_total = count_left + count_right + 1
            count += node.val == sum_total // count_total
            return sum_total, count_total

        solution_1562_4_2(root)
        return count