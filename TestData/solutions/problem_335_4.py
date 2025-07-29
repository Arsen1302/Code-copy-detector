class Solution:
    def solution_335_4(self, root: Optional[TreeNode]) -> int:
        mp = {None: 0}
        ans = 0 
        prev = None
        node = root
        stack = []
        while node or stack: 
            if node: 
                stack.append(node)
                node = node.left
            else: 
                node = stack[-1]
                if node.right and prev != node.right: node = node.right 
                else: 
                    mp[node] = node.val + mp[node.left] + mp[node.right]
                    ans += abs(mp[node.left] - mp[node.right])
                    stack.pop()
                    prev = node 
                    node = None 
        return ans