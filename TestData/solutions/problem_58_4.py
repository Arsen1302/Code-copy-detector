class Solution:
    def solution_58_4(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        post_order, stack = [], []
        node = root
        while stack or node:
            while node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                node = node.left
            last = stack.pop()
            if last.right and stack and last.right == stack[-1]:
                node = stack.pop()
                stack.append(last)
            else:
                post_order.append(last.val)
        return post_order