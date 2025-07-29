class Solution:
    def solution_1087_3(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        even_idx = True
        while len(queue):
            for i in range(len(queue)):
                node = queue.popleft()
                if node == '$':
                    continue
                if even_idx and node.val%2 == 0:
                    return False
                elif not even_idx and node.val%2!= 0:
                    return False
                if even_idx:
                    # strictly decreasing order 
                    if queue and queue[0]!='$' and node.val >= queue[0].val:
                        return False
                elif not even_idx:
                    if queue and queue[0]!='$' and node.val <= queue[0].val:
                        print('called')
                        return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if queue:        
                queue.append('$')
                    
            even_idx = not even_idx
        return True