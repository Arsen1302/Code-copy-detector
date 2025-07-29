class Solution:
    def solution_300_4(self, root: Optional[TreeNode]) -> List[int]:
        values = {}
        
        q = deque()
        q.append((root, 0))
        
        while q:
            node, depth = q.popleft()
            
            if not node:
                continue
                
            if depth not in values:
                values[depth] = node.val
            else:
                values[depth] = max(values[depth], node.val)
            
            q.append((node.left, depth + 1))
            q.append((node.right, depth + 1))
            
        return [x for x in values.values()]