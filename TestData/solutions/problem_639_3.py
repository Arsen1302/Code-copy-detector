class Solution:
    def solution_639_3(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        missing = False
        while q:
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                if node.left:
                    if missing:
                        return False            
                    q.append(node.left)
                else:
                    missing = True
                if node.right:
                    if missing:
                        return False
                    q.append(node.right)
                else:
                    missing = True
                    
        return True