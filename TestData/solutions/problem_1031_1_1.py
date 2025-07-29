class Solution:
    def solution_1031_1_1(self, root: TreeNode, distance: int) -> int:
        
        def solution_1031_1_2(node):
            """Return (a list of) distances to leaves of sub-tree rooted at node."""
            nonlocal ans
            if not node: return []
            if node.left is node.right is None: return [0]
            left,right = solution_1031_1_2(node.left), solution_1031_1_2(node.right)
            ans += sum(2 + x + y <= distance for x in left for y in right)
            return [1 + x for x in left + right]
        
        ans = 0
        solution_1031_1_2(root)
        return ans