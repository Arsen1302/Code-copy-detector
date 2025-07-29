class Solution:
    def solution_23_3_1(self, root: TreeNode) -> bool:
        def solution_23_3_2(node):
            if not node:
                return 0
            return 1 + max(solution_23_3_2(node.left), solution_23_3_2(node.right))
        
        if not root:
            return True
        return abs(solution_23_3_2(root.left) - solution_23_3_2(root.right)) <= 1 and \
                self.solution_23_3_1(root.left) and self.solution_23_3_1(root.right)