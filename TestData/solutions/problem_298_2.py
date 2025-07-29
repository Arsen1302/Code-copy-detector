class Solution:
    def solution_298_2(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        last = 0
        
        while len(queue):
            node = queue.pop(0)
            last = node.val
            
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
                
                
        return last