class Solution:
    def solution_583_2(self, root: TreeNode) -> TreeNode:
        node = root
        stack = []
        prev = None
        lowest = None
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:    
                node = stack.pop()
                if not lowest:
                    lowest = node
                node.left = None
                if prev:
                    prev.right = node
                prev = node
                node = node.right
        return lowest