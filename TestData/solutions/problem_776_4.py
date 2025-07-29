class Solution:
    def solution_776_4(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        tracker = [float('-inf'),0]
        q.append(root)
        level = 1
		
        while q:
            levelSum = 0
            for _ in range(len(q)):
                node = q.popleft()
                levelSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if levelSum > tracker[0]:
                tracker[0] = levelSum
                tracker[1] = level
            level += 1
			
        return tracker[1]