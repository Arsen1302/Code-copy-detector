class Solution:
    def solution_42_1_1(self, root: Optional[TreeNode]) -> int:
        def solution_42_1_2(node, num):
            if node is None:
                return 0
            num = num * 10 + node.val
            if node.left is None and node.right is None:
                return num
            return solution_42_1_2(node.left, num) + solution_42_1_2(node.right, num)
        
        return solution_42_1_2(root, 0)