class Solution:
    def solution_1087_5(self, root: Optional[TreeNode]) -> bool:

        from collections import deque
        queue = deque([(root, 0)])
        depth = defaultdict(list)
        depth[0] = [root.val]
        if root.val %2 == 0:
            return False
        while queue:
            node, d = queue.popleft()
          
            if len(depth[d]) == 0:
                if d %2 == 0 and node.val %2 == 0:
                    return False
                elif d %2 ==1 and node.val %2 ==1:
                    return False
                else:
                    depth[d].append(node.val)
            else:
                if d>0 and d %2 == 0:
                    if node.val <= depth[d][-1] or node.val %2 ==0:
                  
                        return False
                if d>0 and d % 2 ==1:
                    if node.val >= depth[d][-1] or node.val %2 ==1:
                    
                        return False
                depth[d].append(node.val)
            if node:
                if node.left:
                    queue.append((node.left, d+1))
                if node.right:
                    queue.append((node.right, d+1))
        
        return True