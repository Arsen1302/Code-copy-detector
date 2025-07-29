class Solution:
    def solution_1031_2_1(self, root: TreeNode, distance: int) -> int:
        ans = 0
        
        def solution_1031_2_2(node): 
            """Return distances of leaves of sub-tree rooted at node."""
            nonlocal ans 
            if not node: return []
            if node.left is node.right is None: return [0]
            left, right = solution_1031_2_2(node.left), solution_1031_2_2(node.right)
            for x in right: 
                k = bisect_right(left, distance - x - 2) # binary search 
                ans += k
            # merge 
            out = []
            i = j = 0 
            while i < len(left) or j < len(right): 
                if j == len(right) or i < len(left) and left[i] < right[j]: 
                    out.append(1 + left[i])
                    i += 1
                else:
                    out.append(1 + right[j])
                    j += 1
            return out
        
        solution_1031_2_2(root)
        return ans