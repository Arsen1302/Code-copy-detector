class Solution:
    def solution_552_1_1(self, root: TreeNode) -> TreeNode:
        
        @lru_cache(None)
        def solution_552_1_2(node):
            """Return height of tree rooted at node."""
            if not node: return 0
            return 1 + max(solution_552_1_2(node.left), solution_552_1_2(node.right))
        
        node = root
        while node: 
            left, right = solution_552_1_2(node.left), solution_552_1_2(node.right)
            if left == right: return node
            elif left > right: node = node.left
            else: node = node.right