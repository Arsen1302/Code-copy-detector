class Solution:
    def solution_382_5_1(self, root: Optional[TreeNode]) -> List[List[str]]:
        @cache
        def solution_382_5_2(root):
            if root is None:
                return 0
            return 1 + max(solution_382_5_2(root.left), solution_382_5_2(root.right))
        
        root_height = solution_382_5_2(root)
        
        h = root_height #solution_382_5_2
        w = 2**(h)-1 #width
        
        twoDArr = [[""]*w for _ in range(h)]
        
        #BFS Traversal
        stack = [[root, [0, (w-1)//2]]]
        while stack:
            next_queue = []
            while len(stack) > 0:
                cell = stack.pop()
                node = cell[0]
                [r,c] = cell[1]
                
                twoDArr[r][c] = str(node.val)
                if node.left:
                    next_queue.append([node.left, [r+1, c-2**(h-r-2)]])
                if node.right:
                    next_queue.append([node.right, [r+1, c+2**(h-r-2)]])
            stack = next_queue
        return twoDArr