class Solution:
    def solution_1087_1(self, root: TreeNode) -> bool:
        even = 1 # even level 
        queue = deque([root])
        while queue: 
            newq = []
            prev = -inf if even else inf
            for _ in range(len(queue)): 
                node = queue.popleft()
                if even and (node.val&amp;1 == 0 or prev >= node.val) or not even and (node.val&amp;1 or prev <= node.val): return False 
                prev = node.val 
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            even ^= 1
        return True