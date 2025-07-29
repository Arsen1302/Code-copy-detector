class Solution:
    def solution_298_5(self, root: TreeNode) -> int:
        q = collections.deque()
        q.append(root)
        bottom_left = root.val
        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if i == 0:
                    bottom_left = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return bottom_left