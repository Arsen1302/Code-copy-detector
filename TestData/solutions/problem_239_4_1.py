class Solution:
    def solution_239_4_1(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Sum up from root to each depth and check if it's equal to targetSum
        def solution_239_4_2(root, path):
            if not root:
                return
            path += root.val
            if path == targetSum:
                nonlocal sum_count
                sum_count += 1
            solution_239_4_2(root.left, path)
            solution_239_4_2(root.right, path)

        # Send each node to solution_239_4_2 function
        def solution_239_4_3(root):
            if not root:
                return
            solution_239_4_2(root, 0)
            solution_239_4_3(root.left)
            solution_239_4_3(root.right)

        sum_count = 0
        solution_239_4_3(root)
        return sum_count