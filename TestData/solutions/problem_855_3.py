class Solution:
    def solution_855_3(self, root: TreeNode) -> int:
        ans = 0
        queue = deque([root])
        while queue: 
            val = 0
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node: 
                    val += node.val 
                    queue.append(node.left)
                    queue.append(node.right)
            if val: ans = val 
        return ans