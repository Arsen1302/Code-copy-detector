class Solution:
    def solution_855_2(self, root: TreeNode) -> int:
        queue = [root]
        while queue:
            front = []
            ans = 0
            for node in queue: 
                ans += node.val
                if node.left: front.append(node.left)
                if node.right: front.append(node.right)
            queue = front
        return ans