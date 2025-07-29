class Solution:
    def solution_632_3_1(self, root1: TreeNode, root2: TreeNode) -> bool:
        def solution_632_3_2(node1 = root1, node2 = root2):
            if (not node1) and (not node2):
                return True
            elif (not node1) or (not node2) or (node1.val != node2.val):
                return False
            L1, R1, L2, R2 = node1.left, node1.right, node2.left, node2.right
            if (L1 and L2 and L1.val == L2.val) or (R1 and R2 and R1.val == R2.val):
                return solution_632_3_2(L1, L2) and solution_632_3_2(R1, R2)
            else:
                return solution_632_3_2(L1, R2) and solution_632_3_2(L2, R1)
        return solution_632_3_2()