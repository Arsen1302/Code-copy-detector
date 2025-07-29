class Solution:
    def solution_382_1_1(self, root: TreeNode) -> List[List[str]]:
        height = 0
        def solution_382_1_2(node, h):                               # Find height
            nonlocal height
            height = max(height, h)
            if node.left:
                solution_382_1_2(node.left, h+1)
            if node.right:    
                solution_382_1_2(node.right, h+1)
        solution_382_1_2(root, 0)
        n = 2 ** (height + 1) - 1                       # Get `n`
        offset = (n - 1) // 2                           # Column for root node
        ans = [[''] * n for _ in range(height + 1)]
        q = [(root, 0, offset)]
        for i in range(height+1):                       # BFS
            tmp_q = []
            while q:
                cur, r, c = q.pop()
                ans[r][c] = str(cur.val)
                if cur.left:
                    tmp_q.append((cur.left, r+1, c-2 ** (height - r - 1)))
                if cur.right:    
                    tmp_q.append((cur.right, r+1, c+2 ** (height - r - 1)))
            q = tmp_q
        return ans