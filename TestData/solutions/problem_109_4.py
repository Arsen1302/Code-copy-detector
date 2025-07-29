class Solution:
    def solution_109_4(self, root: Optional[TreeNode]) -> int:
        queue = []
        if not root:
            return 0
        queue.append(root)
        count = 0
        while queue:
            node = queue.pop(0)
            count += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return count