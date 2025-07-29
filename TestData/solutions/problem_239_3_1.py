class Solution:
    def solution_239_3_1(self, root: TreeNode, sum: int) -> int:
        seen = {0: 1}
        
        def solution_239_3_2(node, prefix):
            """Return number of paths summing to target for tree rooted at node."""
            if not node: return 0 #base condition 
            prefix += node.val # prefix sum up to node 
            ans = seen.get(prefix - sum, 0)
            seen[prefix] = 1 + seen.get(prefix, 0)
            ans += solution_239_3_2(node.left, prefix) + solution_239_3_2(node.right, prefix)
            seen[prefix] -= 1 # backtrack 
            return ans
        
        return solution_239_3_2(root, 0)