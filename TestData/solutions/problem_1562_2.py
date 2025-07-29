class Solution:
    def solution_1562_2(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        mp = {None: (0, 0)}
        node, stack = root, []
        prev = None
        while node or stack: 
            if node: 
                stack.append(node)
                node = node.left 
            else: 
                node = stack[-1]
                if node.right and node.right != prev: node = node.right
                else: 
                    stack.pop()
                    ls, lc = mp[node.left]
                    rs, rc = mp[node.right]
                    sm, cnt = ls + node.val + rs, lc + 1 + rc
                    mp[node] = (sm, cnt)
                    if sm//cnt == node.val: ans += 1
                    prev = node 
                    node = None
        return ans