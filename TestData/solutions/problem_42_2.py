class Solution:
    def solution_42_2(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        stack = [(root, 0)]
        while stack: 
            node, val = stack.pop()
            val = 10*val + node.val 
            if not node.left and not node.right: ans += val 
            if node.left: stack.append((node.left, val))
            if node.right: stack.append((node.right, val))
        return ans