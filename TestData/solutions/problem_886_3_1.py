class Solution:
    def solution_886_3_1(self, root: Optional[TreeNode]) -> int:
        
        sums = []
        def solution_886_3_2(node):
            if node is None:
                return 0
            subtree_sum = solution_886_3_2(node.left) + solution_886_3_2(node.right) + node.val
            sums.append(subtree_sum)
            return subtree_sum
        
        
        m = -inf
        total = solution_886_3_2(root)
        for i in sums:
            prod = i * (total-i)
            if prod > m: m = prod
        
        return m % (10**9 + 7)