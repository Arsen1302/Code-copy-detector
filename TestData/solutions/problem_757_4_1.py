class Solution:
    def solution_757_4_1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Find all the deepest leaves
        q = deque([root])
        
        while q:
            res = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                
                res.append(node.val)

        # find LCA of deepest leaves
        def solution_757_4_2(root):
            if not root:
                return None
            
            if root.val in res:
                return root
            
            left = solution_757_4_2(root.left)
            right = solution_757_4_2(root.right)
            
            if left and right:
                return root
            
            if not left:
                return right
            else:
                return left
        return solution_757_4_2(root)