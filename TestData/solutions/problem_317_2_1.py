class Solution:
    def solution_317_2_1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def solution_317_2_2(node, init):
            if not node: return 0
            
            r_sum = solution_317_2_2(node.right, init)
            orig, node.val = node.val, node.val + init + r_sum
            l_sum = solution_317_2_2(node.left, node.val)
            
            return r_sum + orig + l_sum
                       
        solution_317_2_2(root, 0)
        return root