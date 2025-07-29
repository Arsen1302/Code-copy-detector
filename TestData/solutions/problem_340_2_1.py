class Solution:
    def solution_340_2_1(self, root: TreeNode, subRoot: TreeNode) -> bool:

        def solution_340_2_2(root):
            if not root:
                return "L"
            left_end = "$" if not root.left else ""
            right_end = "#" if not root.right else ""
            return left_end + "|" + solution_340_2_2(root.left) + "-" + str(root.val) + "-" + solution_340_2_2(root.right) + "|" + right_end

        x = solution_340_2_2(subRoot)
        y = solution_340_2_2(root)

        return y.find(x) != -1