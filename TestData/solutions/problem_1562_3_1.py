class Solution:
    def solution_1562_3_1(self, root: Optional[TreeNode]) -> int:
        def solution_1562_3_2(node):
            if not node:
                return (0,0,0)
            left, right = solution_1562_3_2(node.left), solution_1562_3_2(node.right)
            subtree_sum = left[0]+right[0]+node.val
            nodes_in_subtree = left[1]+right[1]+1
            nodes_eq_to_avg = left[2]+right[2]+(subtree_sum//nodes_in_subtree == node.val)
            return (subtree_sum, nodes_in_subtree, nodes_eq_to_avg)
        return solution_1562_3_2(root)[2]