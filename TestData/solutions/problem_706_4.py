class Solution:
    def solution_706_4(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = [[root, root.val, root.val]]
        while stack:
            node, a, b = stack.pop()
            if node.left:
                stack.append([node.left, max(node.left.val, a), min(node.left.val, b)])
                ans = max(ans, stack[-1][1] - stack[-1][2])
            if node.right:
                stack.append([node.right, max(node.right.val, a), min(node.right.val, b)])
                ans = max(ans, stack[-1][1] - stack[-1][2])
        return ans