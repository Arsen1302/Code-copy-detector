class Solution:
    def solution_1720_1(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        queue = deque([root])
        while queue: 
            vals = []
            for _ in range(len(queue)): 
                node = queue.popleft()
                vals.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            mp = {x : i for i, x in enumerate(sorted(vals))}
            visited = [0]*len(vals)
            for i in range(len(vals)): 
                cnt = 0 
                while not visited[i] and i != mp[vals[i]]: 
                    visited[i] = 1
                    cnt += 1
                    i = mp[vals[i]]
                ans += max(0, cnt-1)
        return ans