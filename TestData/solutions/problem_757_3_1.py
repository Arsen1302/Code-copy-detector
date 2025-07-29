class Solution:
    def solution_757_3_1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        maxDepth = 0
        deepestLeaves = 1
        q = collections.deque([(root, 0)])
        
        while q:
            curRoot, curDepth = q.popleft()
            if curDepth > maxDepth:
                maxDepth = curDepth
                deepestLeaves = 0
            deepestLeaves += 1

            if curRoot.left:
                q.append((curRoot.left, curDepth + 1))
            if curRoot.right:
                q.append((curRoot.right, curDepth + 1))
        
        if maxDepth == 0:
            return root
        if deepestLeaves == 1:
            return curRoot
        
        self.lca = None
        self.lcaDepth = -1
        
        def solution_757_3_2(root, curDepth):
            if root is None:
                return 0
            if curDepth == maxDepth:
                return 1
            
            n = solution_757_3_2(root.left, curDepth + 1) + solution_757_3_2(root.right, curDepth + 1)
            if n == deepestLeaves and curDepth > self.lcaDepth:
                self.lca = root
                self.lcaDepth = curDepth
            return n
        
        solution_757_3_2(root, 0)
        return self.lca