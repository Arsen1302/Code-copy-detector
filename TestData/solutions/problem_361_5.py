class Solution:
    def solution_361_5(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1: return TreeNode(val, root)
        
        queue = deque([root])
        while depth - 1 != 1:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            depth -= 1
                
        while queue:
            node = queue.popleft()
            node.left  = TreeNode(val, left  = node.left)
            node.right = TreeNode(val, right = node.right)
            
        return root