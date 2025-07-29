class Solution:
    
    def solution_387_2(self, root: TreeNode) -> int:        
 
        queue = collections.deque([(root, 0, 0)])
    
        left, right = {}, {}
    
        result = 0
    
        while queue:
            node, x, y = queue.popleft()
            if not node: continue
            left[y] = min(left.get(y, x), x)
            right[y] = max(right.get(y, x), x)
            result = max(result, right[y]-left[y]+1)
            queue.extend([
                (node.left, 2*x, y+1),
                (node.right, (2*x)+1, y+1)
            ])
            
        return result